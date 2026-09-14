"""Stage 3 — Scoring (CLAUDE.md §2).

Reads raw submissions from Supabase, scores them with the calibrated
pipeline from scoring/engine.py (imported as-is, not reimplemented), and on
a manual button press replaces the `leaderboard` table wholesale.

This on-screen table is the guaranteed fallback (CLAUDE.md §2, Stage 3): it
must work regardless of what the Cloudflare Pages leaderboard is doing, so
it doesn't call out to anything but Supabase and plain Streamlit widgets.
"""

from datetime import datetime, timezone

import pandas as pd
import streamlit as st
from supabase import create_client

from scoring.data import GATES
from scoring.engine import score_build
from scoring.parse_submission import ParseError, parse_submission

st.set_page_config(page_title="Battle of New York — Scoring", layout="wide")

NIL_UUID = "00000000-0000-0000-0000-000000000000"


@st.cache_resource
def get_client():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]
    except KeyError as e:
        st.error(
            f"Missing secret: {e}. Add SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY "
            f"in Streamlit Cloud's app settings -> Secrets."
        )
        st.stop()
    return create_client(url, key)


def fetch_submissions(client):
    resp = client.table("submissions").select("*").execute()
    return resp.data


def score_all(rows):
    """Returns (scored_entries, errors). Never raises -- a bad row is
    reported, not allowed to take down the whole scoring run."""
    scored, errors = [], []
    for row in rows:
        try:
            parsed = parse_submission(row["payload"])
        except (ParseError, KeyError, TypeError) as e:
            errors.append({"response_id": row.get("response_id"), "error": str(e)})
            continue
        result = score_build(parsed["raw_axis_totals"], parsed["vuln_picks"])
        scored.append({
            "response_id": row["response_id"],
            "created_at": row["created_at"],
            "player_name": parsed["player_name"] or "(unknown)",
            "hero_name": parsed["hero_name"] or "(unnamed hero)",
            "result": result,
        })
    return scored, errors


def sort_key(entry):
    """CLAUDE.md §4, step 8-9: sort descending by total, then break ties by
    (1) gates passed, (2) highest single-axis peak, (3) earlier timestamp."""
    r = entry["result"]
    return (
        -r.total,
        -sum(r.gates_passed.values()),
        -max(r.scaled.values()),
        entry["created_at"],
    )


def build_leaderboard_rows(scored_sorted):
    now = datetime.now(timezone.utc).isoformat()
    rows = []
    for rank, entry in enumerate(scored_sorted, start=1):
        r = entry["result"]
        rows.append({
            "rank": rank,
            "player_name": entry["player_name"],
            "hero_name": entry["hero_name"],
            "total_score": round(r.total, 2),
            "gates_passed": sum(r.gates_passed.values()),
            "gate_detail": r.gates_passed,
            "scored_at": now,
        })
    return rows


def replace_leaderboard(client, rows):
    """Delete-then-insert, always (CLAUDE.md L21) -- never append, so a
    scoring run can never leave a mixed-generation leaderboard on screen."""
    client.table("leaderboard").delete().neq("id", NIL_UUID).execute()
    if rows:
        client.table("leaderboard").insert(rows).execute()


def clear_database(client):
    """Admin-only, pre-event reset. Wipes both tables using the same
    delete-then-neq-nil pattern as replace_leaderboard -- no second
    deletion mechanism, no raw SQL."""
    client.table("submissions").delete().neq("id", NIL_UUID).execute()
    client.table("leaderboard").delete().neq("id", NIL_UUID).execute()


@st.dialog("Clear Database")
def confirm_clear_database(client):
    st.warning(
        "Are you sure? This will DELETE all rows in `submissions` AND "
        "`leaderboard` tables."
    )
    col1, col2 = st.columns(2)
    if col1.button("Yes, delete everything", type="primary", use_container_width=True):
        try:
            clear_database(client)
            st.session_state["clear_db_status"] = ("success", "Tables cleared ✓")
        except Exception as e:
            st.session_state["clear_db_status"] = ("error", f"Failed to clear tables: {e}")
        st.session_state["show_clear_confirm"] = False
        st.rerun()
    if col2.button("Cancel", use_container_width=True):
        st.session_state["show_clear_confirm"] = False
        st.rerun()


def display_table(scored_sorted):
    display_rows = []
    for rank, entry in enumerate(scored_sorted, start=1):
        r = entry["result"]
        row = {
            "Rank": rank,
            "Player": entry["player_name"],
            "Hero": entry["hero_name"],
            "Total": round(r.total, 1),
            "Gates": f"{sum(r.gates_passed.values())}/5",
        }
        for gate in GATES:
            row[gate["label"]] = "✅" if r.gates_passed[gate["key"]] else "❌"
        display_rows.append(row)
    st.dataframe(pd.DataFrame(display_rows), use_container_width=True, hide_index=True)


client = get_client()

with st.sidebar.expander("⚠️ Admin Controls", expanded=False):
    st.caption("Destructive. Use before the event or between test runs only.")
    if st.button("Clear Database"):
        st.session_state["show_clear_confirm"] = True

    if st.session_state.get("show_clear_confirm"):
        confirm_clear_database(client)

    status = st.session_state.pop("clear_db_status", None)
    if status:
        kind, msg = status
        (st.success if kind == "success" else st.error)(msg)

st.title("Build Your Hero — Scoring Console")
st.caption(
    "Stage 3 fallback display (CLAUDE.md §2). This view never depends on the "
    "Cloudflare Pages leaderboard, Realtime, or custom styling -- it's the one "
    "that has to work no matter what."
)

run = st.button("Run Scoring", type="primary")

if run:
    with st.spinner("Fetching submissions from Supabase..."):
        rows = fetch_submissions(client)

    if not rows:
        st.warning("No submissions in the `submissions` table yet.")
    else:
        scored, errors = score_all(rows)
        scored.sort(key=sort_key)
        leaderboard_rows = build_leaderboard_rows(scored)

        with st.spinner("Replacing leaderboard table (delete-then-insert)..."):
            replace_leaderboard(client, leaderboard_rows)

        st.session_state["scored"] = scored
        st.session_state["errors"] = errors
        st.success(
            f"Scored {len(scored)} of {len(rows)} submissions. "
            f"Leaderboard replaced with {len(leaderboard_rows)} rows."
        )

if "scored" in st.session_state:
    st.subheader("Leaderboard")
    display_table(st.session_state["scored"])

if st.session_state.get("errors"):
    st.subheader(f"Parse warnings ({len(st.session_state['errors'])})")
    st.caption(
        "These submissions were skipped -- not scored, not on the leaderboard. "
        "The raw payload is still in Supabase untouched, so nothing is lost; "
        "re-run once the issue is understood."
    )
    for e in st.session_state["errors"]:
        st.warning(f"{e['response_id']}: {e['error']}")

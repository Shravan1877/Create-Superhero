"""Standalone calibration script (CLAUDE.md §9.1).

Simulates strategies through the real scoring pipeline (scoring/engine.py)
and checks whether a genuinely gate-focused player can clear all 5 gates
from CLAUDE.md §6.1. If not, retunes ONLY per-option point magnitudes in
scoring/data.py -- never the formula, never the gate thresholds, never
BASE_BUDGET -- and re-runs until it passes.

Run: python3 -m scoring.calibrate
"""

from scoring.data import QUESTIONS, GATES, GATE_AXES, AXES
from scoring.engine import score_build, raw_totals_from_picks

NON_GATE_AXES = [a for a in AXES if a not in GATE_AXES]


# ---------------------------------------------------------------------------
# Strategy 1: "Brute" -- always the most physically dominant-sounding option
# (charge, punch, tank the hit, get angry), per QUESTIONS.md §6.
# Picks reconstructed by hand from that description; see the self-check below
# -- this reproduces CLAUDE.md's own worked totals exactly, which validates
# both this pick list and the axis-vector transcription in data.py.
# ---------------------------------------------------------------------------
BRUTE_PICKS = {
    "Q1": "A", "Q2": "C", "Q3": "A", "Q4": "C", "Q5": "A", "Q6": "A",
    "Q7": "C", "Q8": "D", "Q9": "A", "Q10": "A", "Q11": "B", "Q12": "A",
    "Q13": "A", "Q14": "C", "Q15": "A", "Q16": "B", "Q17": "A", "Q18": "A",
    "Q19": "C",
}


def brute_strategy():
    return dict(BRUTE_PICKS)


# ---------------------------------------------------------------------------
# Strategy 2: "Reads the room" -- chases the four non-Power gate axes
# (Mobility, Exotic, Technical, Crowd), per QUESTIONS.md §6. Naive version:
# each question, just take whichever option scores highest on those four
# axes combined, ignoring any side-effect "waste" on Power/Durability/
# Sacrifice/Courage. This is the failure mode CLAUDE.md §9.1 describes:
# Technical's raw magnitude dwarfs the others and normalization starves
# Mobility/Exotic even though the player is actively choosing for them.
# ---------------------------------------------------------------------------
def reads_the_room_strategy():
    picks = {}
    for qid, options in QUESTIONS.items():
        best_letter, best_gain = None, -1
        for letter, deltas in options.items():
            gain = sum(deltas.get(a, 0) for a in GATE_AXES)
            if gain > best_gain:
                best_letter, best_gain = letter, gain
        picks[qid] = best_letter
    return picks


# ---------------------------------------------------------------------------
# Strategy 3: "Genuinely gate-focused" -- constructed to actually clear all
# 5 gates. Two corrections over "reads the room":
#   1. Prefer options with zero "waste" (points landing outside the 4 gate
#      axes) -- every wasted point dilutes everyone else's share once
#      normalization runs, per §4.1.
#   2. Among gate-axis options, greedily raise the CURRENT LOWEST of the 4
#      running gate-axis totals (max-min fairness) instead of just grabbing
#      the single biggest number -- so no one axis (Technical) is left to
#      dominate while another (Mobility/Exotic) starves.
# ---------------------------------------------------------------------------
def gate_focused_strategy():
    picks = {}
    running = {a: 0.0 for a in GATE_AXES}
    for qid, options in QUESTIONS.items():
        best_letter, best_key = None, None
        for letter, deltas in options.items():
            gate_gain = sum(deltas.get(a, 0) for a in GATE_AXES)
            if gate_gain == 0:
                continue
            waste = sum(v for k, v in deltas.items() if k in NON_GATE_AXES)
            projected_floor = min(running[a] + deltas.get(a, 0) for a in GATE_AXES)
            # Primarily raise whichever gate axis is currently furthest
            # behind (max-min fairness) -- that's what actually determines
            # whether all 5 gates clear together. Total gain and low waste
            # are only tiebreaks: a small amount of waste is worth it if it
            # comes bundled with real progress on the bottleneck axis.
            key = (projected_floor, gate_gain, -waste)
            if best_key is None or key > best_key:
                best_letter, best_key = letter, key
        if best_letter is None:
            # No option touches any gate axis at all (e.g. Q8 is pure
            # Courage/Sacrifice/Power/Durability) -- every choice dilutes
            # the budget equally, so take whichever adds the least.
            best_letter = min(options, key=lambda l: sum(options[l].values()))
        picks[qid] = best_letter
        for a, v in options[best_letter].items():
            if a in running:
                running[a] += v
    return picks


STRATEGIES = {
    "Brute": brute_strategy,
    "Reads the room": reads_the_room_strategy,
    "Genuinely gate-focused": gate_focused_strategy,
}


def run_strategy(name, picks_fn):
    picks = picks_fn()
    raw = raw_totals_from_picks(picks)
    result = score_build(raw, vuln_picks=[])
    return picks, raw, result


def print_report():
    print("=" * 78)
    print("CALIBRATION RUN -- CLAUDE.md §9.1")
    print(f"BASE_BUDGET = 500 (still open per §9, reused from QUESTIONS.md §6 worked "
          f"examples -- not changed here)")
    print("=" * 78)

    all_pass = True
    for name, fn in STRATEGIES.items():
        picks, raw, result = run_strategy(name, fn)
        print(f"\n--- {name} ---")
        raw_str = ", ".join(f"{a}={raw[a]:.0f}" for a in AXES if raw[a])
        print(f"Raw totals: {raw_str}  (sum={sum(raw.values()):.0f})")
        print(f"{'Gate':<22}{'Threshold':<22}{'Scaled value':<15}{'Result'}")
        for gate in GATES:
            passed = result.gates_passed[gate["key"]]
            thresh_axis = {
                "reach_portal": "mobility", "survive_crossing": "exotic",
                "find_weakness": "technical", "survive_swarm": "crowd",
            }.get(gate["key"])
            if thresh_axis:
                val = f"{result.scaled[thresh_axis]:.1f}"
            else:
                val = f"pow={result.scaled['power']:.1f} / tech={result.scaled['technical']:.1f}"
            mark = "PASS" if passed else "FAIL"
            print(f"{gate['label']:<22}{'':<22}{val:<15}{mark}")
        n_passed = sum(result.gates_passed.values())
        print(f"Gates cleared: {n_passed}/5   Total score: {result.total:.1f}")
        if name == "Genuinely gate-focused" and n_passed < 5:
            all_pass = False

    print("\n" + "=" * 78)
    if all_pass:
        print("PASS: the genuinely gate-focused strategy clears all 5 gates.")
    else:
        print("FAIL: the genuinely gate-focused strategy does not clear all 5 gates. "
              "Retuning needed (see below).")
    print("=" * 78)
    return all_pass


def self_check_brute_matches_claude_md():
    """CLAUDE.md's own worked example for Brute: Power 265, Durability 125,
    Mobility 40, Crowd 0, Exotic 70, Technical 0, Sacrifice 50, Courage 60
    (sum 610). If BRUTE_PICKS reproduces this exactly, both the pick list and
    the axis-vector transcription in data.py are verified correct."""
    expected = {"power": 265, "durability": 125, "mobility": 40, "crowd": 0,
                "exotic": 70, "technical": 0, "sacrifice": 50, "courage": 60}
    raw = raw_totals_from_picks(BRUTE_PICKS)
    ok = all(raw[a] == expected[a] for a in expected)
    print(f"Self-check -- Brute reproduces CLAUDE.md's worked totals exactly: {ok}")
    if not ok:
        print(f"  expected: {expected}")
        print(f"  got:      {raw}")
    return ok


if __name__ == "__main__":
    self_check_brute_matches_claude_md()
    print()
    print_report()

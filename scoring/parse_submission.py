"""Turns a raw Tally webhook payload (the `submissions.payload` JSONB column)
into the inputs scoring/engine.py needs: raw per-axis totals and a
vulnerability pick list.

Matches purely on question/option TEXT, never on Tally's internal field keys
or option UUIDs -- see the note in scoring/data.py. If a form rebuild changes
those texts, this raises instead of silently mis-scoring; nothing here is
guessed.
"""

from typing import Any, Dict, List

from scoring.data import (
    AXES, QUESTIONS, QUESTION_PROMPTS, OPTION_TEXT, INTRO_LABELS,
    VULN_PROMPT, VULNERABILITIES,
)

_PROMPT_TO_QID = {text: qid for qid, text in QUESTION_PROMPTS.items()}
_OPTION_TEXT_TO_LETTER = {
    (qid, text): letter
    for qid, opts in OPTION_TEXT.items()
    for letter, text in opts.items()
}
_VULN_TEXT_TO_KEY = {v["text"]: key for key, v in VULNERABILITIES.items()}


class ParseError(Exception):
    pass


def parse_submission(payload: Dict[str, Any]) -> Dict[str, Any]:
    fields = payload["data"]["fields"]

    player_name = None
    hero_name = None
    raw = {axis: 0 for axis in AXES}
    vuln_picks: List[str] = []
    seen_questions = set()

    for field in fields:
        label = (field.get("label") or "").strip()

        if label == INTRO_LABELS["player_name"]:
            player_name = field.get("value")
            continue
        if label == INTRO_LABELS["hero_name"]:
            hero_name = field.get("value")
            continue

        if label in _PROMPT_TO_QID:
            qid = _PROMPT_TO_QID[label]
            selected = field.get("value") or []
            if not selected:
                continue  # required in the form; an empty answer is a skip, not an error
            options_by_id = {o["id"]: o["text"] for o in field.get("options", [])}
            selected_text = (options_by_id.get(selected[0]) or "").strip()
            letter = _OPTION_TEXT_TO_LETTER.get((qid, selected_text))
            if letter is None:
                raise ParseError(
                    f"{qid}: selected option text {selected_text!r} doesn't match "
                    f"any known option -- form text may have drifted from scoring/data.py"
                )
            for axis, points in QUESTIONS[qid][letter].items():
                raw[axis] += points
            seen_questions.add(qid)
            continue

        if label == VULN_PROMPT and field.get("type") == "CHECKBOXES":
            options_by_id = {o["id"]: o["text"] for o in field.get("options", [])}
            for opt_id in (field.get("value") or []):
                text = (options_by_id.get(opt_id) or "").strip()
                key = _VULN_TEXT_TO_KEY.get(text)
                if key is None:
                    raise ParseError(f"vulnerability text {text!r} doesn't match any known card")
                vuln_picks.append(key)
            continue

        # Anything else (Tally's exploded per-option CHECKBOXES boolean
        # sub-fields, stray metadata) carries no scoring signal -- ignored.

    missing = set(QUESTION_PROMPTS) - seen_questions
    if missing:
        raise ParseError(f"missing answers for: {sorted(missing)}")
    if len(vuln_picks) > 3:
        raise ParseError(f"more than 3 vulnerabilities selected: {vuln_picks}")

    return {
        "player_name": player_name,
        "hero_name": hero_name,
        "raw_axis_totals": raw,
        "vuln_picks": vuln_picks,
    }

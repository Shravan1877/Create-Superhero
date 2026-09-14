"""The scoring pipeline (CLAUDE.md §4). Pure arithmetic, no branching on
trait polarity, deterministic. This module is the one place scoring logic
lives (L18) -- Streamlit imports it as-is in Phase 4.

Pipeline order is load-bearing, per §4:
    budget -> normalize -> axis score -> gates -> vuln penalty -> total
"""

from dataclasses import dataclass, field
from typing import Dict, List

from scoring.data import AXES, GATES, VULNERABILITIES, BASE_BUDGET, GATE_BONUS, VULN_SCALE


@dataclass
class ScoreResult:
    raw: Dict[str, float]
    budget: float
    scaled: Dict[str, float]
    axis_contributions: Dict[str, float]
    axis_score: float
    gates_passed: Dict[str, bool]
    gate_bonus_total: float
    vuln_penalty: float
    total: float
    vuln_picks: List[str] = field(default_factory=list)


def compute_budget(vuln_picks: List[str], base_budget: float = BASE_BUDGET) -> float:
    return base_budget + sum(VULNERABILITIES[v]["budget_grant"] for v in vuln_picks)


def normalize(raw: Dict[str, float], budget: float) -> Dict[str, float]:
    """scaled = raw * (budget / raw.sum()), clipped at 100 (CLAUDE.md §4.1)."""
    total = sum(raw.get(axis, 0) for axis in AXES)
    if total <= 0:
        return {axis: 0.0 for axis in AXES}
    scale = budget / total
    return {axis: min(raw.get(axis, 0) * scale, 100.0) for axis in AXES}


def axis_scores(scaled: Dict[str, float]) -> Dict[str, float]:
    """contribution = weight * (100 - abs(actual - optimum)), per §4.2."""
    return {
        axis: cfg["weight"] * (100 - abs(scaled[axis] - cfg["optimum"]))
        for axis, cfg in AXES.items()
    }


def check_gates(scaled: Dict[str, float]) -> Dict[str, bool]:
    return {gate["key"]: bool(gate["check"](scaled)) for gate in GATES}


def vuln_penalty(vuln_picks: List[str], scale: float = VULN_SCALE) -> float:
    return sum(
        VULNERABILITIES[v]["severity"] * VULNERABILITIES[v]["exploitability"]
        for v in vuln_picks
    ) / scale


def score_build(raw: Dict[str, float], vuln_picks: List[str] = None,
                 base_budget: float = BASE_BUDGET) -> ScoreResult:
    vuln_picks = vuln_picks or []
    assert len(vuln_picks) <= 3, "max 3 vulnerabilities (CLAUDE.md L6)"

    budget = compute_budget(vuln_picks, base_budget)
    scaled = normalize(raw, budget)
    contributions = axis_scores(scaled)
    axis_score = sum(contributions.values())
    gates = check_gates(scaled)
    gate_bonus_total = GATE_BONUS * sum(gates.values())
    penalty = vuln_penalty(vuln_picks)
    total = axis_score + gate_bonus_total - penalty

    return ScoreResult(
        raw=raw, budget=budget, scaled=scaled,
        axis_contributions=contributions, axis_score=axis_score,
        gates_passed=gates, gate_bonus_total=gate_bonus_total,
        vuln_penalty=penalty, total=total, vuln_picks=vuln_picks,
    )


def raw_totals_from_picks(picks: Dict[str, str]) -> Dict[str, float]:
    """picks: {question_id: option_letter} -> summed raw axis totals."""
    from scoring.data import QUESTIONS
    raw = {axis: 0.0 for axis in AXES}
    for qid, letter in picks.items():
        for axis, points in QUESTIONS[qid][letter].items():
            raw[axis] += points
    return raw

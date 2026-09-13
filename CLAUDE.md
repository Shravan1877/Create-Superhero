# CLAUDE.md — Project Technical Contract

> **Read this file completely before doing anything on this project.**
> This file exists to prevent drift. If anything in a conversation contradicts
> this file, **this file wins** unless Sravan explicitly says otherwise.
> When a decision changes, edit this file *in the same turn* — never leave the
> file stale and rely on conversation memory.

---

## 0. Project summary

**What:** A browser-based "build a superhero" game for a university fest activity segment.
**Theme:** The Avengers (2012) — Battle of New York.
**Players:** ~20, each on their own device.
**Premise:** Each player allocates attributes and accepts weaknesses to construct a
hero. The hero is scored against the Chitauri invasion force. Highest score wins.
**Owner:** Sravan (proposed the idea, now building it).
**Deadline:** Needs to be testable same-day.
**Stack:** Tally (form) → Supabase (storage) → Python/Streamlit (scoring) → Cloudflare Pages (projector). GitHub hosts the repo, connected to both Streamlit Community Cloud and Cloudflare Pages for deploys.

---

## 1. Prime directive

> **Stability beats cleverness. Every time. Without exception.**

This runs live in front of an audience with no second attempt. A boring thing that
works is infinitely better than an elegant thing that throws an exception on stage.

Concrete consequences of this directive:

| Rule | Reason |
|---|---|
| **Scoring never leaves Python** | The pipeline is written, tested and verified. Reimplementing it in SQL, TypeScript or Apps Script duplicates logic in a language that isn't built for it — and a bug there decides who wins |
| Storage layer stays dumb | Supabase stores and serves. It does not score, rank, or transform |
| No auth beyond a single anon key | Fewer credentials, fewer failure modes |
| Pure arithmetic scoring | No solver, no model, no randomness |
| Deterministic output | Same submissions in → same leaderboard out, always |
| Human triggers the scoring run | Nothing scores automatically; Sravan presses the button |
| Laptop is always the fallback | Streamlit shows the scored table regardless of what the projector is doing |

**If a proposal adds a dependency, a network call, or a branch — it is probably wrong.**

> **Revision note (architecture change).** Earlier versions of this file said
> "No database — another service to be down" and used manual CSV export between
> stages. That was reversed deliberately, not drifted into. Reason: Google
> Sheets' publish-to-web CSV is a *snapshot*, not a live feed — Google does not
> guarantee it refreshes promptly, and the documented fix is to stop publishing
> and republish. A leaderboard that silently serves stale scores is a worse
> failure than a service being down, because nobody notices. Supabase replaces
> it with a real API. The prime directive didn't change; the thing that best
> satisfies it did.

---

## 2. Architecture — four stages, decoupled

```
STAGE 1            STAGE 2              STAGE 3               STAGE 4
Tally form    →    Supabase        →    Streamlit        →    Cloudflare Pages leaderboard
(collection)       (storage)            (scoring, Python)     (projector)

   webhook          submissions          reads + scores        Realtime
   real-time JSON   table (JSONB)        writes leaderboard    auto-updates
```

Each stage is **independently operable**. A failure in one does not cascade.

### Stage 1 — Collection
- Tally form, filled on players' phones.
- **Zero custom backend.** Tally owns uptime.
- On submit, Tally fires a webhook (free on all Tally plans) carrying the
  response as structured JSON.

### Stage 2 — Storage
- A Supabase Edge Function receives the webhook and does exactly one thing:
  `INSERT` the raw payload into `submissions`. **No scoring, no parsing, no
  branching.** If this function grows past ~20 lines, something has gone wrong.
- Postgres holds raw answers as JSONB. Nothing is transformed on write.

### Stage 3 — Scoring
- Streamlit app, hosted on **Streamlit Community Cloud**, connected to the
  GitHub repo. Reads `submissions` via `supabase-py`,
  runs the **existing verified Python pipeline** (§4), writes results to the
  `leaderboard` table.
- Triggered by a button press. Nothing scores automatically.
- **The on-screen table here is the guaranteed-working fallback.** It must never
  depend on the Cloudflare Pages leaderboard, custom CSS, or anything cosmetic.

### Stage 4 — Reveal
- Static HTML/CSS/JS on Cloudflare Pages. Subscribes to the `leaderboard` table via
  Supabase Realtime and re-renders when it changes.
- No build step, no framework, no backend. One file, drag-and-drop deploy.

> **Locked decision:** there is **no automatic failure detection** between
> Stage 3 and Stage 4. If the projector page misbehaves, Sravan switches the
> display to the Streamlit Cloud tab already open in his browser. Auto-fallback
> logic is itself a thing that can break.

### 2.1 Pre-event checklist (free-tier warm-ups)

Two services on this stack go idle and need a nudge if untouched: Supabase
free-tier projects pause after 7 days with no requests (10–30s cold-start to
recover), and Streamlit Community Cloud apps sleep after 12 idle hours (visitor
gets a "waking up" screen). Neither matters if both are touched the same day.

- [ ] Open the Cloudflare Pages leaderboard once before doors open — this alone
      warms Supabase, since the page immediately queries it
- [ ] Open the Streamlit Cloud app URL once before doors open — wakes it from sleep
- [ ] Submit one test response end-to-end, confirm it reaches Supabase and scores
- [ ] Delete the test row before real submissions start
- [ ] Leave Streamlit's browser tab open for the whole event — don't close it between the warm-up and the actual scoring run

---

## 3. Data contracts

Two Postgres tables. Raw answers in, scored results out. Nothing is transformed
on write — all transformation happens in Stage 3, in Python.

### 3.1 `submissions` — written by the Edge Function

| Column | Type | Notes |
|---|---|---|
| `id` | `uuid` PK | `default gen_random_uuid()` |
| `created_at` | `timestamptz` | `default now()` — also the tiebreak field |
| `response_id` | `text` UNIQUE | Tally's own response ID; **prevents duplicate inserts on webhook retry** |
| `payload` | `jsonb` | The entire Tally webhook body, untouched |

`payload` stays raw on purpose. If the question-to-column mapping turns out
wrong on event day, the original answers are still there to re-parse — no
re-collection needed.

### 3.2 `leaderboard` — written by Streamlit, read by Cloudflare Pages

| Column | Type | Notes |
|---|---|---|
| `id` | `uuid` PK | |
| `rank` | `int` | 1 = winner |
| `player_name` | `text` | |
| `hero_name` | `text` | |
| `total_score` | `numeric` | |
| `gates_passed` | `int` | 0–5 |
| `gate_detail` | `jsonb` | Which specific gates passed, for the ✅/❌ row |
| `scored_at` | `timestamptz` | |

Streamlit **replaces** this table on each scoring run (delete-all then insert),
never appends. One run = one complete, consistent leaderboard. No partial state.

### 3.3 Access model

| Table | anon key | service role |
|---|---|---|
| `submissions` | no access | full (Edge Function) |
| `leaderboard` | **read only** | full (Streamlit) |

RLS on for both. The Cloudflare Pages leaderboard ships the anon key publicly — that's expected
and safe, because anon can only read the already-public leaderboard. It cannot
read raw submissions and cannot write anything.

### 3.4 Reference data (stays in code, not the database)

Axis weights/optimums, gate thresholds, the vulnerability table, and the
question→score lookup all live in the Python source. They are configuration,
not data — versioned in git, not editable mid-event.

---

## 4. Scoring pipeline — exact order of operations

**This order is load-bearing. Do not reorder.**

```
1. LOAD          fetch rows from Supabase `submissions`, parse payload
2. BUDGET        budget = BASE_BUDGET + Σ(budget_grant of chosen vulns)
3. NORMALIZE     rescale each player's raw axis values to sum to `budget`
4. AXIS SCORE    per axis: weight × (100 − |actual − optimum|)
5. GATES         per gate: if threshold met, add gate bonus
6. VULN PENALTY  subtract Σ(severity × exploitability) / SCALE
7. TOTAL         sum of 4 + 5 − 6
8. SORT          descending by total
9. TIEBREAK      see §4.4
```

### 4.1 Normalization — the anti-max mechanism

```python
scaled = raw * (budget / raw.sum())
```

**Purpose:** a player who maxes every axis and a player who fills every axis with
the same low number produce the *identical* build. Raw magnitude is meaningless;
only the **shape** of the allocation matters.

This converts the greedy strategy from *winning* into *generic*. It requires no
form validation, no rejected submissions, and no error messages.

**Post-scale clip:** cap each scaled axis at 100 (`min(scaled, 100)`) before it
enters §4.2. Raw per-axis sums aren't bounded by construction — a heavily-touched
axis (see §9.1) can scale past 100. The clip only affects axes that already
cleared their optimum; it never changes a gate pass/fail.

### 4.2 Axis scoring — one formula, zero branches

```python
contribution = weight * (100 - abs(actual - optimum))
```

Every axis — physical, mental, personality — uses this identical line.
There is **no** `if positive / elif negative / elif double_edged`.
Trait polarity is expressed entirely through the `optimum` number:

| Trait shape | `optimum` value |
|---|---|
| "More is better" | 100 |
| "Less is better" | low (e.g. 15) |
| "Double-edged" | mid (e.g. 55–75) |

> **Locked decision:** polarity is a *number*, never a category.
> Rationale: three code paths = three places to have a bug.

### 4.3 Gates — why flat builds lose

Normalization alone makes a flat build *average*. Gates make it **fail**.

Gates are pass/fail thresholds derived from the actual Chitauri mission (§6).
A flat, normalized build sits near the mean on every axis and clears almost none
of them — because the win condition has a *specific shape*, not a high average.

```python
if value >= threshold:
    total += gate_bonus
```

Deterministic. Explainable to a crowd in one sentence.

### 4.4 Tie-breaking

Applied in order until resolved:
1. Higher number of gates passed
2. Higher single-axis peak (rewards commitment to a specialty)
3. Earlier `timestamp`

Never random. The result must be reproducible and defensible if challenged live.

---

## 5. Anti-drift guards — things to NOT do

These are mistakes that are tempting mid-conversation. Do not make them.

| ❌ Don't | ✅ Instead |
|---|---|
| Suggest vector embeddings / cosine similarity / "regression" | Weighted sum + gates. There is **no training data**; "regression" here would be a weighted sum in disguise with extra failure modes |
| Add ML, solvers, or optimization libraries | Arithmetic |
| Make the player form expose all 22 axes | Expose a curated 6–8 subset (§7) |
| Add auto-detect / auto-fallback logic | Manual toggle |
| Put scoring logic in SQL, an Edge Function, or Apps Script | Python only — see L18 |
| Let the Edge Function parse, validate, or score | It inserts. That's all |
| Make the Cloudflare Pages leaderboard poll on a timer | Realtime subscription |
| Append to `leaderboard` instead of replacing | Delete-then-insert, always |
| Ship the service-role key to Cloudflare Pages | anon key only — it's read-only on one table |
| Silently change an `optimum` or `weight` | Change it in SUPERHEROES.md and say so |
| Invent hero ratings without interrogation | Follow the interrogation protocol in SUPERHEROES.md |
| Let raw magnitude affect score | Normalization always runs first |
| Use randomness anywhere | Deterministic only |

---

## 6. Enemy model — the Chitauri (locked research)

The scoring targets are derived from canon, not invented. Summary:

**Force composition:** infantry (cybernetically enhanced, armor fused to body,
human-level durability), chariots (fast, unarmored, exposed crew), Leviathans
(colossal armored troop carriers, slow, weaker where armor doesn't cover),
Command Ship (beyond the portal).

**Key strengths:** endless reinforcement through the portal; hive-mind coordination
with no fear and no morale cost; Leviathan armor that Iron Man could not penetrate
from outside.

**The keystone weakness:** every unit is neurally linked to the mothership.
Destroy it and the entire army instantly deactivates. One strike ends the war.

**Design consequence — the single most important idea in this project:**

> A hero built purely for raw strength **loses**. Punching Chitauri one at a time
> never ends; there are always more. The real win condition is
> **reach the portal → survive the crossing → identify the weakness → destroy the mothership.**
> That rewards flight, vacuum survivability, and *technical intelligence* over brute force.

This is why the game is interesting instead of "everyone maxes Strength and ties."

### 6.1 Gate definitions

| Gate | Requirement | Canon justification |
|---|---|---|
| Reach the portal | Mobility & Flight ≥ 70 | Ground-bound heroes never get there |
| Survive the crossing | Exotic Survivability ≥ 70 | Vacuum, no oxygen — Stark nearly died |
| Find the weakness | Technical Intelligence ≥ 75 | The Avengers *didn't know* the weakness |
| Crack a Leviathan | Raw Power ≥ 85 **OR** Technical Int ≥ 80 | Hulk/Thor smash it; Stark killed one from inside |
| Survive the swarm | Crowd Clearing ≥ 60 | Infinite reinforcements |

> Thresholds are **provisional** until validated against the hero dataset.
> Validation status: see SUPERHEROES.md §7.

---

## 7. The form ≠ the framework

**The 22-axis framework is the scoring backbone. It is NOT the player form.**

Nobody at a fest fills out 22 sliders. The form exposes a curated **6–8 axes** plus
vulnerability selection. The remaining axes either don't apply to player builds or
are derived.

This keeps the dataset rich without punishing the players.

---

## 8. Locked decisions (with rationale)

| # | Decision | Rationale |
|---|---|---|
| L1 | Four decoupled stages, manual handoffs | Each handoff is an error checkpoint |
| L2 | Weighted buckets + gates, **not** vector similarity | No training data exists; explainability matters live |
| L3 | Polarity as `optimum` number, not category | Eliminates all branching |
| L4 | Normalization before scoring | Makes max-everything mathematically flat |
| L5 | Vulnerabilities grant budget | The only way to get more points is to accept a real flaw |
| L6 | Max 3 vulnerabilities | Caps budget runaway; keeps CSV flat |
| L7 | Roster-relative 0–100 scale | Absolute scale squashes all humans into 5–15 |
| L8 | Severity **and** Exploitability, not one number | "Catastrophic but untriggerable" ≠ "mild but constant" |
| L9 | Manual view toggle, no auto-fallback | Fallback logic is itself breakable |
| L10 | Deterministic tie-breaks | Must be defensible if challenged on stage |
| L11 | Stage 1 theme: light, background white, text near-black `#14141A` | Clean, high-contrast, native to Tally's free tier |
| L12 | Accent color `#E23636` (buttons, links, selected states, focus rings) | Vibrant — a color choice only, not a depiction of any character |
| L13 | Cover block: solid color `#1560D4`, not an image | Free-tier way to get a second vibrant color, no custom CSS/Pro needed |
| L14 | Font: **Manrope**, single family for headline and body | Wide weight range (200–800) carries both without pairing, which the free tier doesn't support |
| L15 | Structural pattern: phase headers + dividers per Block A/B/C, columns for paired sliders, icon images on vulnerability cards, progress bar | Makes the free-tier form feel designed, not default |
| L16 | Form provider: **Tally** | Genuinely free tier (unlimited forms/submissions, conditional logic, free AI form builder) plus a real MCP connector for Claude Code |
| L17 | Storage: **Supabase Postgres**, not Google Sheets | Sheets' publish-to-web CSV is a snapshot with no refresh guarantee — it serves stale data silently, which is the worst failure mode for a live reveal |
| L18 | **Scoring stays in Python.** Never SQL, never TypeScript, never Apps Script | The pipeline is already written and verified; duplicating it elsewhere puts the thing that decides the winner in an untested reimplementation |
| L19 | Edge Function does INSERT only | Any logic there is logic in the wrong language. >20 lines = something went wrong |
| L20 | `response_id` UNIQUE constraint | Webhooks retry on failure; this makes double-submission impossible at the database level rather than in code |
| L21 | Streamlit replaces the leaderboard table wholesale each run | Delete-then-insert means no partial or mixed-generation state can ever display |
| L22 | Cloudflare Pages leaderboard reads via Realtime subscription | Leaderboard updates itself the moment scoring runs — no refresh button, no polling |
| L23 | Raw `payload` stored as JSONB, never parsed on write | If column mapping is wrong on the day, answers are re-parseable without re-collecting |

---

## 9. Open decisions (not yet locked)

- [ ] `BASE_BUDGET` final value and per-axis point-value calibration — see §9.1
- [ ] Gate bonus magnitude vs. axis score magnitude
- [ ] `SCALE` divisor for the vulnerability penalty
- [ ] Whether to show players their hero vs. a matched canonical Avenger

**Resolved this session:**
- Form provider: **Tally** (L16)
- Player-facing axes and question set: **see QUESTIONS.md** — 8 exposed axes
  (Raw Power, Durability, Mobility & Flight, Crowd Clearing, Exotic Survivability,
  Technical Intelligence, Self-Sacrifice, Courage Under Terror), 19 scenario
  questions + 1 vulnerability multi-select
- Vulnerability list: **see QUESTIONS.md** — 10 universal vulnerability cards,
  max 3 picks

### 9.1 Calibration flag (found while designing the questions)

QUESTIONS.md's worked example shows Technical Intelligence currently accumulates
raw points far faster than Mobility, Exotic Survivability, or Crowd Clearing
across the 19 questions — Tech was deliberately woven in as a secondary axis on
many options, since "the weakness had to be discovered" is the whole thesis (see
ENEMY.md §8.4). Left uncorrected, this crowds out the other gate axes after
normalization even for a deliberately gate-focused player — see the worked
example's second player.

**Before trusting the §6.1 thresholds on real submissions:** run a small
calibration script — simulate a few strategies (pure brute, gate-focused, random)
through the actual scoring pipeline, and retune per-option point magnitudes (not
the formula, not the gate thresholds) until a genuinely gate-focused player can
clear all five. This is a Stage 2 pre-launch task, not a live-event task.

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **Axis** | One rated attribute, 0–100 |
| **Block** | Group of axes — A (Physical), B (Mind), C (Personality) |
| **Optimum** | The value that scores best on an axis |
| **Weight** | How much an axis matters for this mission |
| **Gate** | Pass/fail threshold tied to a mission step |
| **Budget** | Total points a player may distribute |
| **Keystone** | The Chitauri mothership link — the army's single point of failure |
| **Flat build** | A build with near-equal allocation everywhere. Should lose. |
| **Edge Function** | Supabase serverless endpoint. Here: receives the Tally webhook, inserts one row, nothing else |
| **Realtime** | Supabase's live-subscription feature. The projector page listens to `leaderboard` and re-renders on change |
| **anon key** | Public Supabase key, safe to ship in client JS. Read-only on `leaderboard`, no access to `submissions` |
| **service-role key** | Privileged Supabase key. Stays in Streamlit Cloud's secrets manager and in the Edge Function's environment. Never in git, never in the browser |

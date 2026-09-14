# QUESTIONS.md — The Player Form, Question by Question

> Companion to `CLAUDE.md`, `SUPERHEROES.md`, and `ENEMY.md`. This file resolves
> two open items from `CLAUDE.md` §9: which axes the player form exposes, and
> what the actual 20 questions are. It also resolves the vulnerability list.
>
> **Design constraint, stated plainly:** players never see numbers, sliders, or
> axis names. They see 19 scenario questions and one "pick your weaknesses"
> question. Every option is flavor text. The scoring vector behind each option
> is invisible to the player — which is *why* this works. A slider labeled "Raw
> Power" invites someone to drag it to 100 even though it's pointless once
> normalized. A scenario question with four narratively distinct options doesn't
> offer that move at all — there's no "max everything" option to reach for.

---

## 1. The 8 exposed axes

`CLAUDE.md` §7 already decided the form exposes a curated subset, not all 22
framework axes. Here's the subset and why each one made the cut:

| Axis | Why it's exposed |
|---|---|
| **Raw Power** | Gate-adjacent (`Crack a Leviathan` OR-branch); the obvious "strength" stat every player expects to see reflected somewhere |
| **Durability** | Second-heaviest Block A weight (8); "can you take a hit" is intuitive and fun to ask about |
| **Mobility & Flight** | **Gate-critical** — `Reach the portal` |
| **Crowd Clearing** | **Gate-critical** — `Survive the swarm` |
| **Exotic Survivability** | **Gate-critical** — `Survive the crossing` |
| **Technical Intelligence** | **Gate-critical** (two gates) and the single heaviest weight in the entire framework (10) |
| **Self-Sacrifice Drive** | Heaviest personality weight (10) — this *is* the nuke-run question |
| **Courage Under Terror** | Tied-heaviest personality weight (10) — the other half of the nuke-run question |

Five of these eight are load-bearing for the mission gates in `CLAUDE.md` §6.1.
The other three carry real scoring weight and give the quiz emotional range.
Everything else in the 22-axis framework (Leadership, Improvisation, the other
eight personality traits, etc.) stays in the reference dataset only — it never
reaches the player.

---

## 2. Intro fields (not scored, not part of the 20)

| Field | Prompt |
|---|---|
| `player_name` | "Your name" |
| `hero_name` | "Your hero's name — make it good, it's going on the leaderboard" |

---

## 3. The 19 scenario questions

**Language rule for this section:** no invented alien names, no military
jargon. A player who has never seen *The Avengers* should be able to read any
question here and immediately picture the moment. "The giant flying ship
shaped like a whale" does the same job as "a Leviathan" without requiring
anyone to have done homework. Scoring vectors are unchanged from the first
draft — only the words changed.

Each question is a moment lifted from the Battle of New York (`ENEMY.md` Part
IV) or the mission's decisive act. The **scoring** column is invisible to the
player; it's the Stage 2 lookup table.

### Q1 — First contact
*The sky rips open above the city. Alien soldiers and small flying attack bikes are already pouring out. Your first move:*

| Option | Text | Scoring |
|---|---|---|
| A | Run straight at the nearest group, fists first | Power +25, Durability +10 |
| B | Get up high before anyone even notices you | Mobility +30, Courage +5 |
| C | Wait a few seconds longer than feels safe, just watching how they move together | Technical +30, Courage +5 |
| D | Stand your ground in the street so the people behind you can get away | Durability +25, Sacrifice +10 |

### Q2 — The flying bike attack
*One of the small flying attack bikes swings around and starts shooting at a crowd of people running for cover. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Put your body between them and the blast | Durability +15, Sacrifice +20 |
| B | Figure out where it's headed and cut it off before it can shoot again | Technical +20, Mobility +10 |
| C | Rip a car door off and throw it straight at the driver | Power +30 |
| D | Grab as many people as you can carry and get them out | Mobility +15, Crowd +15 |

### Q3 — The drop
*A hatch opens on the huge flying ship above you, and two dozen alien soldiers drop straight onto your street. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Wade in and start swinging — one at a time is fine by you | Power +25, Durability +10 |
| B | Find the one narrow spot they all have to squeeze through | Technical +20, Crowd +15 |
| C | Light up the whole block at once | Crowd +30 |
| D | You don't fight this one. You get everyone else off this block instead | Sacrifice +15, Mobility +15 |

### Q4 — The giant in the sky
*The huge flying ship turns and comes straight for you. Its armor just shrugged off actual tank shells. Your move:*

| Option | Text | Scoring |
|---|---|---|
| A | Hit it exactly where two armor plates meet — the one soft spot | Technical +25, Power +10 |
| B | Get inside it before it gets you, and wreck it from where the armor can't protect it | Technical +20, Exotic +10, Sacrifice +5 |
| C | Hit it so hard the armor stops mattering | Power +35 |
| D | Lead it somewhere emptier before it can do real damage | Mobility +20, Technical +10 |

### Q5 — The nagging thought
*You start to notice this whole army is being controlled by something you can't see. Everyone else is still busy fighting the crowd of soldiers. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Keep swinging. Somebody's got to hold this street | Power +20, Durability +10 |
| B | Start asking why none of them ever panic or run, even when they're clearly losing | Technical +30, Courage +5 |
| C | Decide the crowd of soldiers isn't the real fight, and go look for the real one | Technical +20, Sacrifice +10 |
| D | Trust that someone smarter is already working the problem, and cover them instead | Durability +15, Courage +15 |

### Q6 — Getting up there
*The hole in the sky the aliens are pouring out of is a hundred floors up, with gunfire flying on every side. Getting up there means:*

| Option | Text | Scoring |
|---|---|---|
| A | Climbing, fighting, clawing your way up building by building | Power +15, Durability +15 |
| B | Just going. Straight up, straight through | Mobility +35 |
| C | Waiting for an opening someone else creates | Courage +10, Durability +10 |
| D | Deciding you were never getting up there, and making peace with fighting down here instead | Sacrifice +5, Durability +20 |

### Q7 — No air up here
*You made it through the hole in the sky. There's no air out here, and barely any light. Your body:*

| Option | Text | Scoring |
|---|---|---|
| A | Was never built for this. You white out fast | Exotic +5, Courage +5 |
| B | Holds together somehow. You don't know how much longer | Exotic +20, Durability +10 |
| C | Doesn't even register it as a problem | Exotic +35 |
| D | You brought help — gear, a suit, something that buys you time | Exotic +50, Technical +10 |

### Q8 — The fear
*Something's coming for you in the dark, and you genuinely don't know if you'll walk away from this. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Freeze for half a second too long | Courage +5, Durability +5 |
| B | Feel the fear and go anyway | Courage +30 |
| C | Stop thinking about yourself entirely and think only about finishing this | Courage +20, Sacrifice +15 |
| D | Get angry instead of scared, and let that carry you | Courage +15, Power +15 |

### Q9 — The decision
*You find it — the thing controlling every soldier down below. Destroying it means going in alone, with no way to call for backup if it goes wrong. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Don't hesitate. This is exactly what you came here to do | Sacrifice +30, Courage +10 |
| B | Hesitate for one real second, then go anyway | Sacrifice +20, Courage +15 |
| C | Look for literally any other option first | Technical +15, Sacrifice +5 |
| D | This isn't a decision you're built to make alone, and you know it | Technical +10, Durability +5 |

### Q10 — Finding the weak spot
*There's no button to press. You have to find the one weak spot on this thing while it's actively trying to kill you. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Just start smashing everything until something breaks | Power +25, Durability +5 |
| B | Read it like a puzzle. There's always a way in | Technical +35 |
| C | You genuinely don't know where to start, and that scares you more than the enemy does | Courage +10, Technical +5 |
| D | You can't solve this. You just buy time for someone who can | Sacrifice +15, Durability +10 |

### Q11 — Boxed in
*Three flying attack bikes surround you in mid-air, guns pointed straight at you. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Dodge and weave until none of them can get a lock on you | Mobility +30 |
| B | Let them come. You can take the hits | Durability +25, Power +5 |
| C | Take out the rider on the closest one and let the crash take the other two | Technical +20, Crowd +10 |
| D | Dive for the ground and lose them in the buildings | Mobility +15, Technical +10 |

### Q12 — The mob
*A whole street's worth of alien soldiers all rush you at once. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Pick the biggest one and go | Power +30 |
| B | Find the one line where hitting once hits five | Crowd +35 |
| C | Get up high. Let the street funnel them somewhere smaller | Mobility +15, Crowd +15 |
| D | You're not built for a fight like this, and you know it fast | Durability +5, Courage +5 |

### Q13 — The ledge
*A civilian is trapped on a ledge, and the huge flying ship is heading straight for the building. You have seconds:*

| Option | Text | Scoring |
|---|---|---|
| A | Go straight through the ship's hull to buy the time | Power +20, Sacrifice +10 |
| B | You're already there. You were fast enough to get there before you'd even finished deciding | Mobility +30 |
| C | You pull the ship's attention away before it reaches the building | Technical +20, Courage +10 |
| D | You physically can't reach them in time, and that's a fact you have to live with | Durability +10, Sacrifice +5 |

### Q14 — Two hours in
*It's been almost two hours. Everyone's running on empty, and there's no sign this ends soon. You:*

| Option | Text | Scoring |
|---|---|---|
| A | The fear caught up a while ago. You're still standing anyway | Courage +30 |
| B | You stopped keeping track of what happens to you a while ago | Sacrifice +20, Courage +10 |
| C | You're coasting on pure physical conditioning at this point | Durability +25, Power +5 |
| D | You're the one still thinking clearly enough to call the next move | Technical +20, Courage +10 |

### Q15 — The clean shot
*You get a clean shot at the hole in the sky itself, mid-fight, no time to plan it out. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Take it. Instinct over thinking it through | Mobility +20, Courage +10 |
| B | You need a second to actually work this out, and you don't have one | Technical +15, Durability +5 |
| C | You go for it, not even knowing what's on the other side | Sacrifice +25, Courage +10 |
| D | You hold position instead — someone better suited should take that shot | Durability +15, Technical +10 |

### Q16 — The dark between worlds
*No air, no gravity you recognize, and something enormous moving in the dark nearby. You:*

| Option | Text | Scoring |
|---|---|---|
| A | Your gear is the only reason you're not already dead out here | Exotic +50, Technical +15 |
| B | Something in your own body just... handles it | Exotic +35 |
| C | You're actively fighting your own body to stay conscious | Exotic +10, Courage +15 |
| D | You brought exactly one plan for this, and you're hoping it holds | Exotic +15, Sacrifice +10 |

### Q17 — The second wave
*A hatch opens on the flying ship right above you — two dozen more soldiers are about to drop. You:*

| Option | Text | Scoring |
|---|---|---|
| A | You don't wait for them to land. You're already climbing the ship itself | Mobility +20, Power +10 |
| B | You already know exactly how many can drop before you have to move | Technical +15, Crowd +20 |
| C | You put yourself between the drop zone and everyone behind you | Durability +20, Sacrifice +10 |
| D | You go for the hatch release itself, not the soldiers | Technical +30 |

### Q18 — The point of no return
*You've found the one weak point in this entire fight, and using it means going somewhere you can't be pulled back from. You:*

| Option | Text | Scoring |
|---|---|---|
| A | You're already moving before you've finished thinking it through | Courage +25, Sacrifice +10 |
| B | You take the extra half-second to be sure | Technical +20, Courage +10 |
| C | You've made peace with not coming back from this one | Sacrifice +30 |
| D | You look for literally any version where you get to walk away too | Technical +15, Sacrifice +10 |

### Q19 — The last wave
*The last wave hits, everyone's exhausted, and there's still more coming through the hole in the sky. You:*

| Option | Text | Scoring |
|---|---|---|
| A | You're still standing purely because you refuse to be the one who stops | Sacrifice +20, Courage +15 |
| B | You clear space faster than they can fill it | Crowd +30 |
| C | You're not tired. You were built for exactly this kind of grind | Durability +25, Power +5 |
| D | You're already three moves ahead of the next wave before it lands | Technical +25, Mobility +5 |

---

## 4. Question 20 — vulnerabilities (max 3)

One multi-select question, framed as a single dramatic beat rather than a
checkbox dump:

> *"Every real hero has a crack in them. Pick up to three that run through yours."*

All ten vulnerabilities score through the **same mechanism** — no per-card
special-casing, matching `CLAUDE.md`'s no-branches philosophy. Each grants
budget on selection; `severity × exploitability` feeds the separate score
penalty in `CLAUDE.md` §4, step 6.

| Card text (shown to player) | Type | Severity | Exploitability | Budget grant | Inspired by |
|---|---|---|---|---|---|
| Your power source can be taken away from you | Dependency | 90 | 50 | +70 | Iron Man / War Machine / Ant-Man |
| Someone you'd drop everything for is out there | Psychological | 75 | 55 | +55 | Hawkeye / Ant-Man / Quicksilver |
| There's a phrase that isn't fully yours to control | Psychological | 95 | 40 | +75 | Winter Soldier — highest severity in the roster |
| You freeze the first time it gets real | Psychological | 70 | 60 | +50 | Scarlet Witch / Quicksilver |
| Your best weapon doesn't work on things that can't feel fear | Situational | 85 | 90 | +65 | Scarlet Witch vs. the hive mind |
| You genuinely can't take a hit | Physical | 88 | 80 | +80 | Black Widow / Hawkeye / Fury |
| Guilt from your past clouds the moment you need clarity most | Psychological | 65 | 50 | +45 | Widow / Banner / Winter Soldier |
| Once you commit, there's no version where you pull back | Situational | 60 | 35 | +35 | Extreme Self-Sacrifice, low external trigger risk |
| Someone else can flip a switch on your own power against your will | Physical | 90 | 35 | +60 | Vision — the Mind Stone |
| The gear keeping you in this fight can be destroyed mid-fight | Dependency | 75 | 65 | +50 | Falcon / Winter Soldier's arm |

**Note on `budget_grant`:** this is a deliberate balancing lever, set by design —
not mechanically derived from severity × exploitability, which is a separate
number feeding the penalty term. A card can be narratively catastrophic and
still grant a modest budget if it's genuinely rare to trigger, and vice versa.

---

## 5. Coverage check — does every axis get enough signal?

Counting every option across all 19 questions that touches each axis at all
(not just the "best" one per question):

| Axis | Times touched |
|---|---|
| Technical Intelligence | 24 |
| Courage Under Terror | 24 |
| Self-Sacrifice Drive | 23 |
| Durability | 22 |
| Raw Power | 16 |
| Mobility & Flight | 14 |
| Exotic Survivability | 9 |
| Crowd Clearing | 8 |

Crowd Clearing and Exotic Survivability being the least-touched is **intentional
and canon-accurate** — in the source material, almost nobody clears these
(Thor alone for Crowd Clearing at scale; Vision and Iron Man alone for Exotic
Survivability). A narrow path is the correct shape for a rare-specialist gate.
Technical Intelligence and Courage running highest is also intentional — they
carry the two heaviest weights in the whole framework. §6 below used to flag
this as unproven ("touched most often" isn't "scaled correctly") — that's now
resolved; see §6 for the retuned numbers.

---

## 6. Worked example — does "pick the strongest option" actually lose?

This is the test that matters. Two players, both answering all 19 questions,
run through the exact pipeline in `CLAUDE.md` §4 (`BASE_BUDGET = 500`, no
vulnerabilities, for a clean comparison).

### Player "Brute" — always picks the most aggressive, most physically dominant option

The realistic failure mode: a player who reads every question for whichever
option *sounds* strongest (charge, punch, tank the hit, get angry) and picks
that, every time, ignoring the other seven axes entirely.

Raw totals: **Power 265, Durability 125, Mobility 40, Crowd 0, Exotic 70,
Technical 0, Sacrifice 50, Courage 60.** (Sum 610.)

After normalizing to budget 500 and clipping at 100:

| Gate | Threshold | Brute's score | Result |
|---|---|---|---|
| Reach the portal | Mobility ≥ 70 | 32.8 | ❌ FAIL |
| Survive the crossing | Exotic ≥ 70 | 57.4 | ❌ FAIL |
| Find the weakness | Technical ≥ 75 | 0 | ❌ FAIL |
| Crack a Leviathan | Power ≥ 85 or Technical ≥ 80 | Power 100 (clipped) | ✅ PASS |
| Survive the swarm | Crowd ≥ 60 | 0 | ❌ FAIL |

**Brute clears 1 of 5 gates.** Despite maxing Power so hard it clips, and never
once picking a "weak-sounding" option, this build cannot reach the portal,
cannot survive leaving the atmosphere, cannot find the weakness, and gets
overrun by the swarm. This is exactly the outcome the whole design exists to
produce: the strongest-*sounding* choice, chosen consistently, loses.

### Player "Reads the room" — deliberately chases the four non-Power gate axes

Raw totals (post-calibration): **Mobility 155, Exotic 110, Technical 220,
Crowd 100, Sacrifice 10, Courage 45, Durability 5, Power 0.** (Sum 645.)

After normalizing to 500 and clipping:

| Gate | Threshold | Score | Result |
|---|---|---|---|
| Reach the portal | Mobility ≥ 70 | 100 (clipped) | ✅ PASS |
| Survive the crossing | Exotic ≥ 70 | 85.3 | ✅ PASS |
| Find the weakness | Technical ≥ 75 | 100 (clipped) | ✅ PASS |
| Crack a Leviathan | Power ≥ 85 or Technical ≥ 80 | Technical 100 | ✅ PASS |
| Survive the swarm | Crowd ≥ 60 | 77.5 | ✅ PASS |

**Reads-the-room now clears 5 of 5** — this used to fail Reach the Portal and
Survive the Crossing narrowly (Technical's raw magnitude dwarfed everything
else and normalization starved the axes this player was actively choosing
for). Fixed by retuning two option magnitudes, not the formula or thresholds:
Q7 option D and Q16 option A (both "brought gear/prepared" flavor, not the
"toughest-sounding" options Brute already picks) had their Exotic values
raised from 25/20 to 50/50. See `CLAUDE.md` §9.1 for the before/after and
`scoring/calibrate.py` for the simulation this was verified against.

*(Numbers are machine-verified against the real scoring engine —
`python3 -m scoring.calibrate` reproduces this exactly.)*

**Independently confirmed live, not just simulated:** a real Tally submission
run through the actual production pipeline (Tally → webhook → Supabase →
scoring) with a deliberately gate-focused pick set scored 4729.17 and cleared
5/5 gates, matching the simulator's prediction exactly. See `CLAUDE.md` §9.2
for a real problem this same test surfaced: that build's *total score*
still ranked below a 2/5-gate build, because `GATE_BONUS` is far too small
relative to axis-score swings. Gates clearing is no longer mathematically
impossible (this section's original concern) — but gates clearing doesn't
yet reliably *win*, which is a separate, still-open calibration item.

---

## 7. What's now resolved vs. still open

**Resolved by this file (and `scoring/calibrate.py`):**
- The 8 exposed axes and why
- All 19 question texts and their scoring vectors
- The 10-card vulnerability list
- Proof that naive "pick the strongest" loses badly (1/5 gates)
- Point magnitudes retuned so a genuinely gate-focused player clears all 5
  gates, not just 3 — verified both in simulation and via one real, live
  submission through the deployed pipeline

**Still open, see `CLAUDE.md` §9:**
- `GATE_BONUS` magnitude — evidenced problem now, not just a placeholder
  (§9.2): gates clearing doesn't currently move total score enough to win
- `VULN_SCALE` divisor for the vulnerability penalty — untested
- `BASE_BUDGET`'s final value — 500 used throughout but not formally locked

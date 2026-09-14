"""Reference data for the scoring pipeline (CLAUDE.md §3.4).

Axis weights/optimums, gate thresholds, the vulnerability table, and the
question->score lookup live here in code, not in the database. This file is
config, not data: change it deliberately and say so, per CLAUDE.md's
anti-drift guards.
"""

# --- Axes (SUPERHEROES.md Block A/B/C, the 8 exposed in QUESTIONS.md §1) ---
# weight/optimum values are lifted verbatim from SUPERHEROES.md §2-4.

AXES = {
    "power":      {"label": "Raw Power",              "weight": 7,  "optimum": 100},
    "durability": {"label": "Durability",              "weight": 8,  "optimum": 100},
    "mobility":   {"label": "Mobility & Flight",        "weight": 10, "optimum": 100},
    "crowd":      {"label": "Crowd Clearing",           "weight": 10, "optimum": 100},
    "exotic":     {"label": "Exotic Survivability",     "weight": 9,  "optimum": 100},
    "technical":  {"label": "Technical Intelligence",   "weight": 10, "optimum": 100},
    "sacrifice":  {"label": "Self-Sacrifice Drive",     "weight": 10, "optimum": 75},
    "courage":    {"label": "Courage Under Terror",     "weight": 10, "optimum": 100},
}

GATE_AXES = ["mobility", "exotic", "technical", "crowd"]

# --- BASE_BUDGET ---
# Still an OPEN decision per CLAUDE.md §9 -- not locked. 500 is the value
# QUESTIONS.md §6 already used for its worked examples, so it's reused here
# for continuity, not re-decided. Do not change without telling Sravan first.
BASE_BUDGET = 500

# --- Gates (CLAUDE.md §6.1) — LOCKED, do not retune thresholds here ---
GATES = [
    {"key": "reach_portal",    "label": "Reach the portal",
     "check": lambda s: s["mobility"] >= 70},
    {"key": "survive_crossing", "label": "Survive the crossing",
     "check": lambda s: s["exotic"] >= 70},
    {"key": "find_weakness",   "label": "Find the weakness",
     "check": lambda s: s["technical"] >= 75},
    {"key": "crack_leviathan", "label": "Crack a Leviathan",
     "check": lambda s: s["power"] >= 85 or s["technical"] >= 80},
    {"key": "survive_swarm",   "label": "Survive the swarm",
     "check": lambda s: s["crowd"] >= 60},
]

# --- Gate bonus / vulnerability SCALE ---
# Both still OPEN per CLAUDE.md §9 ("gate bonus magnitude vs axis score
# magnitude", "SCALE divisor for the vulnerability penalty"). Gate pass/fail
# never depends on these -- they only affect the TOTAL score number, not
# which gates clear. Provisional placeholders until Sravan locks real values.
GATE_BONUS = 20
VULN_SCALE = 100

# --- The 19 scenario questions (QUESTIONS.md §3), verbatim scoring vectors ---
QUESTIONS = {
    "Q1": {"A": {"power": 25, "durability": 10},
           "B": {"mobility": 30, "courage": 5},
           "C": {"technical": 30, "courage": 5},
           "D": {"durability": 25, "sacrifice": 10}},
    "Q2": {"A": {"durability": 15, "sacrifice": 20},
           "B": {"technical": 20, "mobility": 10},
           "C": {"power": 30},
           "D": {"mobility": 15, "crowd": 15}},
    "Q3": {"A": {"power": 25, "durability": 10},
           "B": {"technical": 20, "crowd": 15},
           "C": {"crowd": 30},
           "D": {"sacrifice": 15, "mobility": 15}},
    "Q4": {"A": {"technical": 25, "power": 10},
           "B": {"technical": 20, "exotic": 10, "sacrifice": 5},
           "C": {"power": 35},
           "D": {"mobility": 20, "technical": 10}},
    "Q5": {"A": {"power": 20, "durability": 10},
           "B": {"technical": 30, "courage": 5},
           "C": {"technical": 20, "sacrifice": 10},
           "D": {"durability": 15, "courage": 15}},
    "Q6": {"A": {"power": 15, "durability": 15},
           "B": {"mobility": 35},
           "C": {"courage": 10, "durability": 10},
           "D": {"sacrifice": 5, "durability": 20}},
    "Q7": {"A": {"exotic": 5, "courage": 5},
           "B": {"exotic": 20, "durability": 10},
           "C": {"exotic": 35},
           "D": {"exotic": 50, "technical": 10}},
    "Q8": {"A": {"courage": 5, "durability": 5},
           "B": {"courage": 30},
           "C": {"courage": 20, "sacrifice": 15},
           "D": {"courage": 15, "power": 15}},
    "Q9": {"A": {"sacrifice": 30, "courage": 10},
           "B": {"sacrifice": 20, "courage": 15},
           "C": {"technical": 15, "sacrifice": 5},
           "D": {"technical": 10, "durability": 5}},
    "Q10": {"A": {"power": 25, "durability": 5},
            "B": {"technical": 35},
            "C": {"courage": 10, "technical": 5},
            "D": {"sacrifice": 15, "durability": 10}},
    "Q11": {"A": {"mobility": 30},
            "B": {"durability": 25, "power": 5},
            "C": {"technical": 20, "crowd": 10},
            "D": {"mobility": 15, "technical": 10}},
    "Q12": {"A": {"power": 30},
            "B": {"crowd": 35},
            "C": {"mobility": 15, "crowd": 15},
            "D": {"durability": 5, "courage": 5}},
    "Q13": {"A": {"power": 20, "sacrifice": 10},
            "B": {"mobility": 30},
            "C": {"technical": 20, "courage": 10},
            "D": {"durability": 10, "sacrifice": 5}},
    "Q14": {"A": {"courage": 30},
            "B": {"sacrifice": 20, "courage": 10},
            "C": {"durability": 25, "power": 5},
            "D": {"technical": 20, "courage": 10}},
    "Q15": {"A": {"mobility": 20, "courage": 10},
            "B": {"technical": 15, "durability": 5},
            "C": {"sacrifice": 25, "courage": 10},
            "D": {"durability": 15, "technical": 10}},
    "Q16": {"A": {"exotic": 50, "technical": 15},
            "B": {"exotic": 35},
            "C": {"exotic": 10, "courage": 15},
            "D": {"exotic": 15, "sacrifice": 10}},
    "Q17": {"A": {"mobility": 20, "power": 10},
            "B": {"technical": 15, "crowd": 20},
            "C": {"durability": 20, "sacrifice": 10},
            "D": {"technical": 30}},
    "Q18": {"A": {"courage": 25, "sacrifice": 10},
            "B": {"technical": 20, "courage": 10},
            "C": {"sacrifice": 30},
            "D": {"technical": 15, "sacrifice": 10}},
    "Q19": {"A": {"sacrifice": 20, "courage": 15},
            "B": {"crowd": 30},
            "C": {"durability": 25, "power": 5},
            "D": {"technical": 25, "mobility": 5}},
}

# --- Question/option TEXT, for parsing real Tally submissions -------------
# Tally's own field keys and option UUIDs are per-form and can change if the
# form is ever rebuilt. Matching on the visible text instead means parsing
# stays correct even then -- this is the same reasoning CLAUDE.md §3.1 gives
# for storing `payload` raw: the answers must always be re-parseable.
# Purely additive metadata; QUESTIONS above (letter -> axis deltas) is
# untouched, so the calibrated pipeline in engine.py/calibrate.py is
# unaffected.

INTRO_LABELS = {
    "player_name": "Your name",
    "hero_name": "Your hero's name — make it good, it's going on the leaderboard",
}

QUESTION_PROMPTS = {
    "Q1": "The sky rips open above the city. Alien soldiers and small flying attack bikes are already pouring out. Your first move:",
    "Q2": "One of the small flying attack bikes swings around and starts shooting at a crowd of people running for cover. You:",
    "Q3": "A hatch opens on the huge flying ship above you, and two dozen alien soldiers drop straight onto your street. You:",
    "Q4": "The huge flying ship turns and comes straight for you. Its armor just shrugged off actual tank shells. Your move:",
    "Q5": "You start to notice this whole army is being controlled by something you can't see. Everyone else is still busy fighting the crowd of soldiers. You:",
    "Q6": "The hole in the sky the aliens are pouring out of is a hundred floors up, with gunfire flying on every side. Getting up there means:",
    "Q7": "You made it through the hole in the sky. There's no air out here, and barely any light. Your body:",
    "Q8": "Something's coming for you in the dark, and you genuinely don't know if you'll walk away from this. You:",
    "Q9": "You find it — the thing controlling every soldier down below. Destroying it means going in alone, with no way to call for backup if it goes wrong. You:",
    "Q10": "There's no button to press. You have to find the one weak spot on this thing while it's actively trying to kill you. You:",
    "Q11": "Three flying attack bikes surround you in mid-air, guns pointed straight at you. You:",
    "Q12": "A whole street's worth of alien soldiers all rush you at once. You:",
    "Q13": "A civilian is trapped on a ledge, and the huge flying ship is heading straight for the building. You have seconds:",
    "Q14": "It's been almost two hours. Everyone's running on empty, and there's no sign this ends soon. You:",
    "Q15": "You get a clean shot at the hole in the sky itself, mid-fight, no time to plan it out. You:",
    "Q16": "No air, no gravity you recognize, and something enormous moving in the dark nearby. You:",
    "Q17": "A hatch opens on the flying ship right above you — two dozen more soldiers are about to drop. You:",
    "Q18": "You've found the one weak point in this entire fight, and using it means going somewhere you can't be pulled back from. You:",
    "Q19": "The last wave hits, everyone's exhausted, and there's still more coming through the hole in the sky. You:",
}

OPTION_TEXT = {
    "Q1": {"A": "Run straight at the nearest group, fists first",
           "B": "Get up high before anyone even notices you",
           "C": "Wait a few seconds longer than feels safe, just watching how they move together",
           "D": "Stand your ground in the street so the people behind you can get away"},
    "Q2": {"A": "Put your body between them and the blast",
           "B": "Figure out where it's headed and cut it off before it can shoot again",
           "C": "Rip a car door off and throw it straight at the driver",
           "D": "Grab as many people as you can carry and get them out"},
    "Q3": {"A": "Wade in and start swinging — one at a time is fine by you",
           "B": "Find the one narrow spot they all have to squeeze through",
           "C": "Light up the whole block at once",
           "D": "You don't fight this one. You get everyone else off this block instead"},
    "Q4": {"A": "Hit it exactly where two armor plates meet — the one soft spot",
           "B": "Get inside it before it gets you, and wreck it from where the armor can't protect it",
           "C": "Hit it so hard the armor stops mattering",
           "D": "Lead it somewhere emptier before it can do real damage"},
    "Q5": {"A": "Keep swinging. Somebody's got to hold this street",
           "B": "Start asking why none of them ever panic or run, even when they're clearly losing",
           "C": "Decide the crowd of soldiers isn't the real fight, and go look for the real one",
           "D": "Trust that someone smarter is already working the problem, and cover them instead"},
    "Q6": {"A": "Climbing, fighting, clawing your way up building by building",
           "B": "Just going. Straight up, straight through",
           "C": "Waiting for an opening someone else creates",
           "D": "Deciding you were never getting up there, and making peace with fighting down here instead"},
    "Q7": {"A": "Was never built for this. You white out fast",
           "B": "Holds together somehow. You don't know how much longer",
           "C": "Doesn't even register it as a problem",
           "D": "You brought help — gear, a suit, something that buys you time"},
    "Q8": {"A": "Freeze for half a second too long",
           "B": "Feel the fear and go anyway",
           "C": "Stop thinking about yourself entirely and think only about finishing this",
           "D": "Get angry instead of scared, and let that carry you"},
    "Q9": {"A": "Don't hesitate. This is exactly what you came here to do",
           "B": "Hesitate for one real second, then go anyway",
           "C": "Look for literally any other option first",
           "D": "This isn't a decision you're built to make alone, and you know it"},
    "Q10": {"A": "Just start smashing everything until something breaks",
            "B": "Read it like a puzzle. There's always a way in",
            "C": "You genuinely don't know where to start, and that scares you more than the enemy does",
            "D": "You can't solve this. You just buy time for someone who can"},
    "Q11": {"A": "Dodge and weave until none of them can get a lock on you",
            "B": "Let them come. You can take the hits",
            "C": "Take out the rider on the closest one and let the crash take the other two",
            "D": "Dive for the ground and lose them in the buildings"},
    "Q12": {"A": "Pick the biggest one and go",
            "B": "Find the one line where hitting once hits five",
            "C": "Get up high. Let the street funnel them somewhere smaller",
            "D": "You're not built for a fight like this, and you know it fast"},
    "Q13": {"A": "Go straight through the ship's hull to buy the time",
            "B": "You're already there. You were fast enough to get there before you'd even finished deciding",
            "C": "You pull the ship's attention away before it reaches the building",
            "D": "You physically can't reach them in time, and that's a fact you have to live with"},
    "Q14": {"A": "The fear caught up a while ago. You're still standing anyway",
            "B": "You stopped keeping track of what happens to you a while ago",
            "C": "You're coasting on pure physical conditioning at this point",
            "D": "You're the one still thinking clearly enough to call the next move"},
    "Q15": {"A": "Take it. Instinct over thinking it through",
            "B": "You need a second to actually work this out, and you don't have one",
            "C": "You go for it, not even knowing what's on the other side",
            "D": "You hold position instead — someone better suited should take that shot"},
    "Q16": {"A": "Your gear is the only reason you're not already dead out here",
            "B": "Something in your own body just... handles it",
            "C": "You're actively fighting your own body to stay conscious",
            "D": "You brought exactly one plan for this, and you're hoping it holds"},
    "Q17": {"A": "You don't wait for them to land. You're already climbing the ship itself",
            "B": "You already know exactly how many can drop before you have to move",
            "C": "You put yourself between the drop zone and everyone behind you",
            "D": "You go for the hatch release itself, not the soldiers"},
    "Q18": {"A": "You're already moving before you've finished thinking it through",
            "B": "You take the extra half-second to be sure",
            "C": "You've made peace with not coming back from this one",
            "D": "You look for literally any version where you get to walk away too"},
    "Q19": {"A": "You're still standing purely because you refuse to be the one who stops",
            "B": "You clear space faster than they can fill it",
            "C": "You're not tired. You were built for exactly this kind of grind",
            "D": "You're already three moves ahead of the next wave before it lands"},
}

VULN_PROMPT = "Every real hero has a crack in them. Pick up to three that run through yours."

# --- The 10 vulnerability cards (QUESTIONS.md §4), max 3 picks ---
VULNERABILITIES = {
    "power_source":     {"text": "Your power source can be taken away from you",
                          "type": "Dependency", "severity": 90, "exploitability": 50, "budget_grant": 70},
    "someone_out_there": {"text": "Someone you'd drop everything for is out there",
                           "type": "Psychological", "severity": 75, "exploitability": 55, "budget_grant": 55},
    "trigger_phrase":   {"text": "There's a phrase that isn't fully yours to control",
                          "type": "Psychological", "severity": 95, "exploitability": 40, "budget_grant": 75},
    "freeze":           {"text": "You freeze the first time it gets real",
                          "type": "Psychological", "severity": 70, "exploitability": 60, "budget_grant": 50},
    "weapon_ineffective": {"text": "Your best weapon doesn't work on things that can't feel fear",
                            "type": "Situational", "severity": 85, "exploitability": 90, "budget_grant": 65},
    "cant_take_hit":    {"text": "You genuinely can't take a hit",
                          "type": "Physical", "severity": 88, "exploitability": 80, "budget_grant": 80},
    "guilt":            {"text": "Guilt from your past clouds the moment you need clarity most",
                          "type": "Psychological", "severity": 65, "exploitability": 50, "budget_grant": 45},
    "no_pullback":      {"text": "Once you commit, there's no version where you pull back",
                          "type": "Situational", "severity": 60, "exploitability": 35, "budget_grant": 35},
    "switch_flip":      {"text": "Someone else can flip a switch on your own power against your will",
                          "type": "Physical", "severity": 90, "exploitability": 35, "budget_grant": 60},
    "gear_destroyable": {"text": "The gear keeping you in this fight can be destroyed mid-fight",
                          "type": "Dependency", "severity": 75, "exploitability": 65, "budget_grant": 50},
}

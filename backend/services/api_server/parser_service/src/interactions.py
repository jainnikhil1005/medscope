import json

with open("data/drug_interactions.json") as f:
    INTERACTIONS = json.load(f)

def check_interaction(drugs1: list[str], drugs2: list[str]) -> tuple[str, str]:
    # Compare every pair for known interactions
    for d1 in drugs1:
        for d2 in drugs2:
            key = f"{d1.lower()}_{d2.lower()}"
            if key in INTERACTIONS:
                return "Warning", INTERACTIONS[key]
    return "Safe", "No known interactions"
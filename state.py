import os
import json
from dataclasses import dataclass, asdict

@dataclass
class State:
    last_id: int

def get_state():
    if not os.path.exists("state.json"):
        return State(0)

    with open("state.json", "r") as state_file:
        state_json = json.load(state_file)
        return State(state_json["last_id"])

def save_state(state):
    with open("state.json.tmp", "w") as state_json:
        json.dump(asdict(state), state_json)

    os.replace("state.json.tmp", "state.json")

import json

def read_json(filename):
    with open(filename,"r") as f:
        return json.load(f)

def print_json(data):
    print(json.dumps(data, indent=4))

def give_man_of_the_match(data):
    maxs = max(p["player_score"] for p in data)
    for p in data:
            p["man_of_the_match"]=(p["player_score"]==maxs)
    return data

def save_json(data, filename):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)



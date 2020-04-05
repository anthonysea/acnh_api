import json

def get_fishes():
    '''Load all fish from critters.json'''
    with open('critters.json') as f:
        data = json.load(f)
    
    fish_data = [fish for fish in data if fish['type'] == 'fish']

    return fish_data, 200

def get_fish(fish_id):
    pass

def get_bugs():
    '''Load all bugs from critters.json'''
    with open('critters.json') as f:
        data = json.load(f)

    bug_data = [bug for bug in data if bug['type'] == 'bug']

    return bug_data, 200

def get_bug(bug_id):
    pass
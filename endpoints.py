import json

def get_fishes():
    '''Load all fish from critters.json'''
    with open('critters.json') as f:
        data = json.load(f)
    
    fish_data = [fish for fish in data if fish['type'] == 'fish']

    return fish_data, 200

def get_fish(fish_id):
    with open('critters.json') as f:
        data = json.load(f)
    fish_query = [fish for fish in data if fish['id'] == fish_id]
    if fish_query:
        fish = fish_query[0]
    else:
        return {
            'detail': f'The fish with id {fish_id} does not exist',
            'status': 404,
            'title': 'Fish Not Found',
            'type': 'about:blank',
        }
    return fish, 200

def get_bugs():
    '''Load all bugs from critters.json'''
    with open('critters.json') as f:
        data = json.load(f)

    bug_data = [bug for bug in data if bug['type'] == 'bug']

    return bug_data, 200

def get_bug(bug_id):
    pass
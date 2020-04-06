import json
from models import Critter, CritterSchema, db

def get_fishes():
    '''Load all fish from the database'''
    fish = Critter.query.filter(Critter.critter_type=='fish').all()

    fish_schema = CritterSchema(many=True)
    return fish_schema.dump(fish)

def get_fish(fish_id):
    pass
    # with open('critters.json') as f:
    #     data = json.load(f)
    # fish_query = [fish for fish in data if fish['id'] == fish_id]
    # if fish_query:
    #     fish = fish_query[0]
    # else:
    #     return {
    #         'detail': f'The fish with id {fish_id} does not exist',
    #         'status': 404,
    #         'title': 'Fish Not Found',
    #         'type': 'about:blank',
    #     }
    # return fish, 200

def get_bugs():
    '''Load all bugs from critters.json'''
    bugs = Critter.query.filter(Critter.critter_type=='bug').all()

    bug_schema = CritterSchema(many=True)
    return bug_schema.dump(bugs)

def get_bug(bug_id):
    pass
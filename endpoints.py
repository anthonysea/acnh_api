import json
from models import Critter, CritterSchema, db

def get_fishes():
    '''Load all fish from the database'''
    fish = Critter.query.filter(Critter.critter_type=='fish').all()

    fish_schema = CritterSchema(many=True)
    return fish_schema.dump(fish)

def get_fish(fish_id):
    fish = Critter.query.filter(Critter.id==fish_id, Critter.critter_type=='fish').one_or_none()

    if not fish:
        return {
            'detail': f'The fish with id {fish_id} does not exist',
            'status': 404,
            'title': 'Fish Not Found',
            'type': 'about:blank',
        }

    fish_schema = CritterSchema()
    return fish_schema.dump(fish)

def get_bugs():
    '''Load all bugs from database'''
    bugs = Critter.query.filter(Critter.critter_type=='bug').all()

    bug_schema = CritterSchema(many=True)
    return bug_schema.dump(bugs)

def get_bug(bug_id):
    bug = Critter.query.filter(Critter.id==bug_id, Critter.critter_type=='bug').one_or_none()

    if not bug:
        return {
            'detail': f'The bug with id {bug_id} does not exist',
            'status': 404,
            'title': 'Bug Not Found',
            'type': 'about:blank',
        }

    bug_schema = CritterSchema()
    return bug_schema.dump(bug)
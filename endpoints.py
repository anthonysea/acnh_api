import json
from models import (
    db,
    Critter, CritterSchema,
    Fossil, FossilSchema,
    Villager, VillagerSchema,
)


def get_villagers():
    villagers = Villager.query.all()

    villager_schema = VillagerSchema(many=True)
    return villager_schema.dump(villagers)


def get_villager(villager_id):
    villager = Villager.query.filter(Villager.id==villager_id).one_or_none()

    if not villager:
        return {
            "detail": f"The villager with id {villager_id} does not exist",
            "status": 404,
            "title": "Villager Not Found",
            "type": "about:blank",
        }

    villager_schema = VillagerSchema()
    return villager_schema.dump(villager)


def get_fishes():
    """Load all fish from the database"""
    fish = Critter.query.filter(Critter.critter_type=="fish").all()

    fish_schema = CritterSchema(many=True)
    return fish_schema.dump(fish)


def get_fish(fish_id):
    fish = Critter.query.filter(Critter.id==fish_id, Critter.critter_type=="fish").one_or_none()

    if not fish:
        return {
            "detail": f"The fish with id {fish_id} does not exist",
            "status": 404,
            "title": "Fish Not Found",
            "type": "about:blank",
        }

    fish_schema = CritterSchema()
    return fish_schema.dump(fish)


def get_bugs():
    """Load all bugs from database"""
    bugs = Critter.query.filter(Critter.critter_type=="bug").all()

    bug_schema = CritterSchema(many=True)
    return bug_schema.dump(bugs)


def get_bug(bug_id):
    bug = Critter.query.filter(Critter.id==bug_id, Critter.critter_type=="bug").one_or_none()

    if not bug:
        return {
            "detail": f"The bug with id {bug_id} does not exist",
            "status": 404,
            "title": "Bug Not Found",
            "type": "about:blank",
        }

    bug_schema = CritterSchema()
    return bug_schema.dump(bug)


def get_fossils():
    fossils = Fossil.query.all()

    fossil_schema = FossilSchema(many=True)
    return fossil_schema.dump(fossils)


def get_fossil(fossil_id):
    fossil = Fossil.query.filter(Fossil.id==fossil_id).one_or_none()

    if not fossil:
        return {
            "detail": f"The fossil with id {fossil_id} does not exist",
            "status": 404,
            "title": "Fossil Not Found",
            "type": "about:blank"
        }

    fossil_schema = FossilSchema()
    return fossil_schema.dump(fossil)
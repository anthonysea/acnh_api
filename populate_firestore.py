import firebase_admin, os
from firebase_admin import firestore, credentials

from models import (
    db,
    Critter, CritterSchema,
    Fossil, FossilSchema,
    Villager, VillagerSchema,
)

from build_db import create_json, load_json_data

def init_firestore():
    creds = credentials.Certificate('./acnh-web-app-firebase-adminsdk-5a16h-aa3d4d27e0.json')
    firebase_admin.initialize_app(creds)
    return firestore.client()

def main():
    json_files = ['critters.json', 'fossils.json', 'villagers.json']
    if not all(map(os.path.isfile, json_files)):
        create_json()

    db = init_firestore()

    # data = load_json_data('critters.json')

    # critter_ref = db.collection(u'critters').document(data[0]['name'])
    # critter_ref.set({
    #     u'name': data[0]['name'],
    #     u'image_url': data[0]['image_url']
    # })

    for filename in json_files:
        data = load_json_data(filename)
        if data is -1:
            print(f"Failed to load {filename}")
            return
        
        if filename == 'critters.json':
            for critter in data:
                shadow_size = critter["shadow_size"] if "shadow_size" in critter else None
                critter_ref = db.collection(u'critters').document()
                critter_ref.set({
                    u'name': critter['name'],
                    u'image_url': critter['image_url'],
                    u'price': critter['price'],
                    u'location': critter['location'],
                    u'shadow_size': shadow_size,
                    u'timeday': critter['timeday'],
                    u'seasonality_n': ''.join([str(x) for x in critter['seasonality_n']]),
                    u'seasonality_s': ''.join([str(x) for x in critter['seasonality_s']]),
                    u'critter_type': critter['critter_type']
                })
                print(f"{critter['name']} added")

        elif filename == 'fossils.json':
            for fossil in data:
                fossil_ref = db.collection(u'fossils').document()
                fossil_ref.set({
                    u'name': fossil['name'],
                    u'image_url': fossil['image_url'],
                    u'price': fossil['price'],
                    u'fossil_type': fossil['fossil_type'],
                    u'group': fossil['group']
                })
                print(f"{fossil['name']} added")

        elif filename == 'villagers.json':
            for villager in data:
                villager_ref = db.collection(u'villagers').document()
                villager_ref.set({
                    u'name': villager['name'],
                    u'image_url': villager['image_url'],
                    u'personality': villager['personality'],
                    u'species': villager['species'],
                    u'birthdate_month': villager['birthdate_month'],
                    u'birthdate_day': villager['birthdate_day'],
                    u'catchphrase': villager['catchphrase']
                })
                print(f"{villager['name']} added")

if __name__ == '__main__':
    main()

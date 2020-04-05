import os
from app import create_app
from models import db

if os.path.exists('test.db'):
    os.remove('test.db')

db.create_all(app=create_app())



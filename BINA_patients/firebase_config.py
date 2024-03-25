# BINA_Ppatients/firebase_config.py
import firebase_admin
from django.conf import settings
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)

def get_user_collection():
    # This function now returns a reference to the users collection in Firestore
    return firestore.client().collection('users')

def get_all_users():
    # This function will retrieve all documents in the users collection
    users_ref = get_user_collection()
    return [doc.to_dict() for doc in users_ref.stream()]

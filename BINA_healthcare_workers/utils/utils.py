# BINA_healthcare_workers/utils.py
from django.db import models
import random
import string


class Utils:
    @staticmethod
    def generate_bina_q_id(first_name, last_name, organisation_name, department_name):
        random_part = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        bina_q_id = f"{first_name[:2].upper()}{last_name[:2].upper()}{organisation_name[:3].upper()}{department_name[:3].upper()}-{random_part}"
        return bina_q_id

    @staticmethod
    def generate_temporary_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(characters) for i in range(10))

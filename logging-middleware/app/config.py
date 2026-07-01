import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENTID")
CLIENT_SECRET = os.getenv("CLIENTSECRET")
ACCESS_CODE = os.getenv("ACCESSCODE")
EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
ROLL_NO = os.getenv("ROLLNO")
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://4.224.186.213/evaluation-service"

EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
ROLLNO = os.getenv("ROLLNO")
ACCESSCODE = os.getenv("ACCESSCODE")
CLIENTID = os.getenv("CLIENTID")
CLIENTSECRET = os.getenv("CLIENTSECRET")
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET = os.environ['secret']
ALGORITHM = 'HS256'
# print(SECRET)

def create_token(email: str):
    return jwt.encode({
        "email": email,
        "project": "online judge"
    }, SECRET, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET,algorithms=[ALGORITHM])
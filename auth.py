from jose import jwt

SECRET = 'vansh'
ALGORITHM = 'HS256'


def create_token(email: str):
    return jwt.encode({
        "email": email,
        "project": "fast_api"
    }, SECRET, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET,algorithms=[ALGORITHM])
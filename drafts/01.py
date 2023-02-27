

# Thinking in pure Python, in a simple script, what would be the basic 
# functions to support the JWT authentication processes?


import jwt

def generate_jwt(payload, secret_key, algorithm='HS256'):
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

def decode_jwt(token, secret_key, algorithms=['HS256']):
    payload = jwt.decode(token, secret_key, algorithms=algorithms)
    return payload

def get_auth_header(request):
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return None
    parts = auth_header.split()
    if parts[0].lower() != 'bearer':
        return None
    if len(parts) == 1:
        return None
    if len(parts) > 2:
        return None
    return parts[1]

def get_payload(request, secret_key, algorithms=['HS256']):
    token = get_auth_header(request)
    if token is None:
        return None
    try:
        payload = decode_jwt(token, secret_key, algorithms=algorithms)
    except jwt.exceptions.DecodeError:
        return None
    return payload



def test_get_auth_header_valid_header(self):

    request = {'headers': {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'}}
    expected_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
    get_auth_header(request) == expected_token

def test_get_auth_header_missing_header(self):
    request = {'headers': {}}
    get_auth_header(request) == None

def test_iget_auth_header_nvalid_header(self):
    request = {'headers': {'Authorization': 'InvalidHeader'}}
    get_auth_header(request) == None

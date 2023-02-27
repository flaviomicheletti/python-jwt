import jwt

payload = {"some": "payload"}
secret = "d41d8cd98f00b204e9800998ecf8427e"


#
# generate jwt
#
encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")

"""

print(encoded_jwt)

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg

"""

#
# decode jwt
#
jwt.decode(encoded_jwt, secret, algorithms=["HS256"])


def test_jwt():
    assert payload == {'some': 'payload'}
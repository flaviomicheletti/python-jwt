from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from config import JWT_SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)    
    # check username and password from request form
    if username == 'john' and password == '1234':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'Access granted'})

# if __name__ == '__main__':
#     app.run()

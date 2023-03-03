from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from config import JWT_SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route('/secure-data', methods=['GET'])
@jwt_required()
def secure_data():
    data = {
        'message': 'This is sensitive data that requires authentication.',
        'secret': 'shhh...'
    }
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)

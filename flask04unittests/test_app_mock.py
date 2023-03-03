import json
import unittest
from unittest.mock import patch


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        from app import app

        self.app = app.test_client()

    @patch("app.create_access_token")
    def test_login_success(self, mock):
        mock.return_value = "mock-token"
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"access_token": "mock-token"})

    @patch("app.create_access_token")
    def test_login_failure(self, mock_create_access_token):
        mock_create_access_token.return_value = "mock-token"
        payload = {"username": "john", "password": "wrong-password"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid username or password"})

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")
    def test_protected(self, mock):
        mock.return_value = None
        response = self.app.get("/protected")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Access granted"})


class SecureDataTestCase(unittest.TestCase):
    def setUp(self):
        # from app import app
        from secure_app import app as secure_app

        # self.app = app.test_client()
        self.secure_app = secure_app.test_client()

    @patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")
    def test_secure_data(self, mock):
        mock.return_value = None
        response = self.secure_app.get("/secure-data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                "message": "This is sensitive data that requires authentication.",
                "secret": "shhh...",
            },
        )


# if __name__ == "__main__":
#     unittest.main()

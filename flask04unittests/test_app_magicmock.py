import json
import unittest
from unittest.mock import MagicMock, patch


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        from app import app

        self.app = app.test_client()

    def test_login_success(self):
        mock = MagicMock(return_value="mock-token")
        with patch("app.create_access_token", mock):
            payload = {"username": "john", "password": "1234"}
            response = self.app.post(
                "/login", data=json.dumps(payload), content_type="application/json"
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"access_token": "mock-token"})
        mock.assert_called_once_with(identity="john")

    def test_login_failure(self):
        mock = MagicMock(return_value="mock-token")
        with patch("app.create_access_token", mock):
            payload = {"username": "john", "password": "wrong-password"}
            response = self.app.post(
                "/login", data=json.dumps(payload), content_type="application/json"
            )
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {"message": "Invalid username or password"})
        mock.assert_not_called()

    def test_protected(self):
        mock = MagicMock(return_value=None)
        with patch(
            "flask_jwt_extended.view_decorators.verify_jwt_in_request",
            mock,
        ):
            response = self.app.get("/protected")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"message": "Access granted"})
        mock.assert_called_once()


class SecureDataTestCase(unittest.TestCase):
    def setUp(self):
        from secure_app import app

        self.app = app.test_client()

    def test_secure_data(self):
        mock = MagicMock(return_value=None)
        with patch(
            "flask_jwt_extended.view_decorators.verify_jwt_in_request",
            mock,
        ):
            response = self.app.get("/secure-data")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json,
                {
                    "message": "This is sensitive data that requires authentication.",
                    "secret": "shhh...",
                },
            )
        mock.assert_called_once()


# if __name__ == "__main__":
#     unittest.main()

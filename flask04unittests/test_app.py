import unittest
import json


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        from app import app

        self.app = app.test_client()

    def test_login(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("access_token" in response.json)

    def test_login_failure(self):
        payload = {"username": "john", "password": "wrong-password"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid username or password"})

    def test_protected(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        token = response.json["access_token"]
        headers = {"Authorization": "Bearer " + token}
        response = self.app.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Access granted"})


class SecureDataTestCase(unittest.TestCase):
    def setUp(self):
        from app import app
        from secure_app import app as secure_app

        self.app = app.test_client()
        self.secure_app = secure_app.test_client()

    def test_secure_data(self):
        payload = {"username": "john", "password": "1234"}
        response = self.app.post(
            "/login", data=json.dumps(payload), content_type="application/json"
        )
        token = response.json["access_token"]
        headers = {"Authorization": "Bearer " + token}
        response = self.secure_app.get("/secure-data", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            {
                "message": "This is sensitive data that requires authentication.",
                "secret": "shhh...",
            },
        )


if __name__ == "__main__":
    unittest.main()

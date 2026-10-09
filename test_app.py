import unittest

import app as app_module


class AppTestCase(unittest.TestCase):
    """Tests for the Flask application routes."""

    def setUp(self):
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()

    def test_homepage_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_returns_expected_text(self):
        response = self.client.get("/")
        self.assertIn(b"Hello", response.data)
        self.assertIn(b"Freebuff", response.data)

    def test_health_url_returns_200(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_health_url_returns_ok(self):
        response = self.client.get("/health")
        self.assertIn(b"OOK", response.data)


if __name__ == "__main__":
    unittest.main()
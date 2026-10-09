import os
import signal
import subprocess
import time
import unittest
import urllib.request

import app as app_module

# Cross-platform process kill helper
if os.name == "nt":  # Windows
    import subprocess

    def kill_process_tree(pid):
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True)
else:  # Unix
    def kill_process_tree(pid):
        os.killpg(os.getpgid(pid), signal.SIGTERM)


class AppTestCase(unittest.TestCase):
    """Tests for the Flask application routes."""

    @classmethod
    def setUpClass(cls):
        # Start the Flask app in a background process before running tests
        cls.server_process = subprocess.Popen(
            ["python", "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Wait for the server to be ready (with a longer timeout)
        for _ in range(50):
            try:
                urllib.request.urlopen("http://localhost:5000/", timeout=1)
                break
            except Exception:
                time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        # Kill the server process tree
        kill_process_tree(cls.server_process.pid)
        cls.server_process.wait()

    def setUp(self):
        # Create a test client for each test
        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()

    def test_homepage_returns_200(self):
        """GET / should return a 200 status code."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_returns_expected_text(self):
        """GET / should return the expected greeting."""
        response = self.client.get("/")
        self.assertIn(b"Hello", response.data)
        self.assertTrue(b"Freebuff" in response.data)

    def test_health_url_returns_200(self):
        """GET /health should return a 200 status code."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_health_url_returns_ok(self):
        """GET /health should return a body indicating OK."""
        response = self.client.get("/health")
        self.assertIn(b"OK", response.data)


if __name__ == "__main__":
    unittest.main()

import unittest

from flask import current_app

from tests.base import BaseTest


class BasicTest(BaseTest):

    def test_app_exist(self):
        self.assertTrue(current_app is not None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_404_error(self):
        response = self.client.get("/foo")
        data = response.text
        self.assertEqual(response.status_code, 404)
        self.assertIn("404 Error", data)

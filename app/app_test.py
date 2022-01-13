import unittest
import requests

API_URL = "http://localhost:5000/"

class ApiTestMessage(unittest.TestCase) :
    # Send message
    def test_message_1_send(self):
        url = f"{API_URL}send"
        req_body = {
            "number": "+6282219118993",
            "message": "Terima kasih atas donasi Anda. Semoga berkah."
        }

        req = requests.post(url, json=req_body)
        self.assertEqual(req.status_code, 200)

class ApiTestVendor(unittest.TestCase) :
    # Switch vendor
    def test_vendor_1_change(self):
        url = f"{API_URL}switch"
        req_body = {
            "vendor_id": "vendor3"
        }

        req = requests.post(url, json=req_body)
        self.assertEqual(req.status_code, 201)

    # Avoid null input for vendor_id
    def test_vendor_1_change_null(self):
        url = f"{API_URL}switch"
        req_body = {
            "vendor_id": None
        }

        req = requests.post(url, json=req_body)
        self.assertNotEqual(req.status_code, 201)

    # Switch to not exist vendor
    def test_vendor_1_change_not_exist(self):
        url = f"{API_URL}switch"
        req_body = {
            "vendor_id": "vendor9"
        }

        req = requests.post(url, json=req_body)
        self.assertNotEqual(req.status_code, 201)
    
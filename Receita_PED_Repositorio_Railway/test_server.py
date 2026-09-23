import http.client
import json
import threading
import unittest
from server import make_server

class ServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = "t" * 48
        cls.server = make_server("127.0.0.1", 0, cls.token)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
    def request(self, path, method="GET", auth=False):
        conn = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
        headers = {"Authorization": "Bearer " + self.token} if auth else {}
        conn.request(method, path, headers=headers)
        res = conn.getresponse()
        status, body = res.status, json.loads(res.read())
        conn.close()
        return status, body
    def test_health(self):
        status, body = self.request("/health")
        self.assertEqual(status, 200)
        self.assertFalse(body["clinical_engine"])
    def test_auth(self):
        self.assertEqual(self.request("/v1/instructions")[0], 401)
    def test_instructions(self):
        status, body = self.request("/v1/instructions", auth=True)
        self.assertEqual(status, 200)
        self.assertGreater(len(body["instructions"]), 100)
    def test_clinical_unimplemented(self):
        self.assertEqual(self.request("/v1/prescribe", "POST", True)[0], 501)
    def test_no_arbitrary_files(self):
        self.assertEqual(self.request("/../package-info.json", auth=True)[0], 404)
    def test_token_required(self):
        with self.assertRaises(ValueError):
            make_server("127.0.0.1", 0, "")

if __name__ == "__main__":
    unittest.main()

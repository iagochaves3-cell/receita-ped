from unittest.mock import patch
import test_server

class PrescriptionContractTest(test_server.ServiceTest):
    def test_capabilities_deny_every_regime(self):
        status, body = self.request('/v1/capabilities', auth=True)
        self.assertEqual(status, 200)
        contract = body['prescription_integration']
        self.assertFalse(contract['available'])
        self.assertEqual(contract['validated_regimes'], [])

    def test_reserved_endpoint_and_alias_never_forward(self):
        with patch('server.forward', side_effect=AssertionError('must not forward')):
            for path in ('/v1/pediatric/prescription', '/v1/prescribe'):
                status, body = self.request(path, 'POST', True)
                self.assertEqual(status, 501)
                self.assertIsNone(body['prescription'])
                self.assertIsNone(body['audit'])
                self.assertFalse(body['clinical_validated'])
                self.assertFalse(body['prescribing_authorization'])
                self.assertEqual(body['status'], 'unavailable')

    def test_reserved_endpoint_requires_auth(self):
        self.assertEqual(self.request('/v1/pediatric/prescription', 'POST')[0], 401)

import os
import unittest

USER = os.getenv('VE_USER')
PASSWORD = os.getenv('VE_PASSWORD')

import GetToken
import Geocoder

class GeocodeAppleInc(unittest.TestCase):
    def setUp(self):
        opts = GetToken.OptionsProxy(user=USER, clientip='0.0.0.0', tokenvalidity=15, production=False)
        self.token = GetToken.getToken(opts, PASSWORD)

    def runTest(self):
        geo = Geocoder.Geocoder(token=self.token)
        results = geo.query('The Metreon, San Francisco')
        assert len(results) == 1, (results, 'We expected one result for the Metreon')
        print results


if __name__ == '__main__':
    unittest.main()

import os
import unittest

USER = os.getenv('VE_USER')
PASSWORD = os.getenv('VE_PASSWORD')

import GetToken
import Geocoder

class ReverseGeocodeAppleInc(unittest.TestCase):
    def setUp(self):
        opts = GetToken.OptionsProxy(user=USER, clientip='0.0.0.0', tokenvalidity=15, production=False)
        self.token = GetToken.getToken(opts, PASSWORD)

    def runTest(self):
        geo = Geocoder.Geocoder(token=self.token)
        results = geo.reverse(37.3317, -122.031)
        assert len(results) == 2, (results, 'Expected two entries for Apple, Inc from ReverseGeocode')
        print results


if __name__ == '__main__':
    unittest.main()

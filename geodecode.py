#!/usr/bin/env python

import getpass
import os
import sys
import time

from optparse import OptionParser

import GetToken
import Geocoder

def main():
    _op = OptionParser(usage='%prog [options] latitude longitude')
    _op.add_option('--user', dest='user', help='Virtual Earth Web Services UserID, used for generating tokens')
    _op.add_option('--password', dest='password', help='Virtual Earth Web Services Password, used for generating tokens')
    _op.add_option('--token', dest='token', default='', help='An already generated token (otherwise one will be generated')
    opts, args = _op.parse_args()

    if not opts.token and not opts.user and not opts.password:
        print '===> I need either a token, or a user/password pair!'
        print
        _op.print_help()
        return -1

    token = opts.token
    if not token:
        optsproxy = GetToken.OptionsProxy(user=opts.user, clientip='0.0.0.0', tokenvalidity=15, production=False)
        token = GetToken.getToken(optsproxy, opts.password)

    geo = Geocoder.Geocoder(token=token)
    start = time.time()

    while ((start + 60 * 15) > time.time()):
        print '==> Please enter lat,long as a common-separated pair'
        try:
            line = raw_input(')) ')
            parts = line.split(',')
            assert len(parts) == 2, (parts, 'We need a lat *and* a long')

            latitude = float(parts[0].strip())
            longitude = float(parts[1].strip())

            print geo.reverse(latitude, longitude)

        except KeyboardInterrupt:
            print '==> exiting, thanks for playing...'
            return 0
        except Exception, ex:
            print ex
    return 0


if __name__ == '__main__':
    rc = main()
    sys.exit(rc)

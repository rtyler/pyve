#!/usr/bin/env python

import getpass
import sys

from optparse import OptionParser

try:
    from ZSI.client import AUTH
except ImportError:
    print '==> Failed to import ZSI'
    print '===> Please make sure you have it installed and locatable from PYTHONPATH'
    print '     http://pywebsvcs.sourceforge.net/'
    print 
    sys.exit(-1)

class GetTokenError(Exception):
    pass

class OptionsProxy(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

def getToken(opts, password):
    if not opts.production:
        from staging import CommonService_client
        from staging import CommonService_types
    else:
        from production import CommonService_client
        from production import CommonService_types

    locator = CommonService_client.CommonServiceLocator()
    service = locator.getCommonServiceSoap(auth=(4, opts.user, password))
    request = CommonService_client.GetClientTokenSoapIn()
    request._request = CommonService_types.ns0.GetClientToken_Dec()
    request._specification = CommonService_types.ns0.TokenSpecification_Def(opts.user)
    request._specification._ClientIPAddress = opts.clientip
    request._specification._TokenValidityDurationMinutes = int(opts.tokenvalidity)

    result = service.GetClientToken(request)
    if result.__class__.__name__ == 'GetClientTokenResponse_Holder':
        return result._GetClientTokenResult
    raise GetTokenError('Web service failed to return a proper response! %s' % result)


def main():
    _op = OptionParser()
    _op.add_option('--user', dest='user', help='User ID for Virtual Earth\'s Web Services')
    _op.add_option('--production', dest='production', action='store_true', help='Generate a token for production use')
    _op.add_option('--clientip', dest='clientip', default='0.0.0.0', help='Specify the ClientIPAddress argument for the CommonService.GetClientToken() API')
    _op.add_option('--tokenvalidity', dest='tokenvalidity', default='480', help='Specify to TokenValidityDurationInMinutes argument for CommonService.GetClientToken(), must be between 15 and 480')
    _op.add_option('--password', dest='password', default=None, help='Password for Virtual Earth\'s Web Services')
    opts, args = _op.parse_args()

    if not opts.user:
        print '==> Missing "user" argument'
        print
        _op.print_help()
        return -1

    password = opts.password
    if not opts.password:
        password = getpass.getpass(prompt='Virtual Earth Password: ')
    token = getToken(opts, password)
    print '==> Generated token: %s' % token
    return 0

if __name__ == '__main__':
    rc = main()
    sys.exit(rc)

# vim: set expandtab:

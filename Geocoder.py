
class Address(object):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '<%s at %s> %s\n' % (self.__class__.__name__, hex(id(self)), ', '.join(['%s=%s' % (k, v) for k, v in self.__dict__.iteritems() if isinstance(self.__dict__[k], basestring) or k == 'address']))

    @classmethod
    def addressFromSoapResponse(cls, holder):
        ''' 
            Return an instantiated Address object based on the returned data from the SOAP ReverseGeocode API

            Expected attributes:
                .address
                .displayName
                .confidence
                .entityType
        '''
        # The _Address.__dict__ dictionary looks something like this:
        # {'_District': '', '_PostalCode': '95014-2084', '_FormattedAddress': '1 Infinite Loop, Cupertino, CA 95014-2084', '_AdminDistrict': 'CA', '_CountryRegion': 'United States', '_AddressLine': '1 Infinite Loop', '_Locality': 'Cupertino', '_PostalTown': ''}
        address = dict(((k[1:], v) for k, v in holder._Address.__dict__.iteritems()))
        return cls(displayName=holder._DisplayName, confidence=holder._Confidence, entityType=holder._EntityType, address=address)


class Geocoder(object):
    def __init__(self, *args, **kwargs):
        self.token = kwargs['token']
        self.production = kwargs.get('production')
        
    def reverse(self, latitude, longitude, altitude=0):
        if not self.production:
            from staging import GeocodeService_client
            from staging import GeocodeService_types
        else:
            from production import GeocodeService_client
            from production import GeocodeService_types
        locator = GeocodeService_client.GeocodeServiceLocator()
        service = locator.getBasicHttpBinding_IGeocodeService()
        request = GeocodeService_client.IGeocodeService_ReverseGeocode_InputMessage()
        request._request = GeocodeService_types.ns5.GeocodeRequest_Def(self.token)

        location = GeocodeService_types.ns3.Location_Dec()
        location._Altitude = altitude
        location._Latitude = latitude
        location._Longitude = longitude

        credentials = GeocodeService_types.ns3.Credentials_Dec()
        credentials._ApplicationId = None
        credentials._Token = self.token

        request._request._Location = location
        request._request._Culture = None
        request._request._Credentials = credentials
        request._request._ExecutionOptions = None

        result = service.ReverseGeocode(request)

        results = result._ReverseGeocodeResult._Results._GeocodeResult
        return [Address.addressFromSoapResponse(piece) for piece in results]

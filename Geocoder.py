

class Geocoder(object):
    def __init__(self, *args, **kwargs):
        super(Geocoder, self).__init__(*args, **kwargs)
        self.token = kwargs['token']
        
        if kwargs.get('production'):
            from staging import GeocodeService_client
            from staging import GeocodeService_types
        else:
            from production import GeocodeService_client
            from production import GeocodeService_types

    def reverse(self, latitude, longitude, altitude=0):
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

        return result



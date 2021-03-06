##################################################
# file: GeocodeService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/local/bin/wsdl2py http://dev.virtualearth.net/webservices/v1/geocodeservice/geocodeservice.svc?wsdl
# 
##################################################

from GeocodeService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class GeocodeServiceLocator:
    BasicHttpBinding_IGeocodeService_address = "http://dev.virtualearth.net/webservices/v1/geocodeservice/GeocodeService.svc"
    def getBasicHttpBinding_IGeocodeServiceAddress(self):
        return GeocodeServiceLocator.BasicHttpBinding_IGeocodeService_address
    def getBasicHttpBinding_IGeocodeService(self, url=None, **kw):
        return BasicHttpBinding_IGeocodeServiceSOAP(url or GeocodeServiceLocator.BasicHttpBinding_IGeocodeService_address, **kw)

# Methods
class BasicHttpBinding_IGeocodeServiceSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: Geocode
    def Geocode(self, request, **kw):
        if isinstance(request, IGeocodeService_Geocode_InputMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://dev.virtualearth.net/webservices/v1/geocode/contracts/IGeocodeService/Geocode", **kw)
        # no output wsaction
        response = self.binding.Receive(IGeocodeService_Geocode_OutputMessage.typecode)
        return response

    # op: ReverseGeocode
    def ReverseGeocode(self, request, **kw):
        if isinstance(request, IGeocodeService_ReverseGeocode_InputMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://dev.virtualearth.net/webservices/v1/geocode/contracts/IGeocodeService/ReverseGeocode", **kw)
        # no output wsaction
        response = self.binding.Receive(IGeocodeService_ReverseGeocode_OutputMessage.typecode)
        return response

IGeocodeService_Geocode_InputMessage = GED("http://dev.virtualearth.net/webservices/v1/geocode/contracts", "Geocode").pyclass

IGeocodeService_Geocode_OutputMessage = GED("http://dev.virtualearth.net/webservices/v1/geocode/contracts", "GeocodeResponse").pyclass

IGeocodeService_ReverseGeocode_InputMessage = GED("http://dev.virtualearth.net/webservices/v1/geocode/contracts", "ReverseGeocode").pyclass

IGeocodeService_ReverseGeocode_OutputMessage = GED("http://dev.virtualearth.net/webservices/v1/geocode/contracts", "ReverseGeocodeResponse").pyclass

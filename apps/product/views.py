from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status

# Create your views here.

from . import credentials
import datetime
import ee
import ee.mapclient

class MaxNdviView(APIView):

    serializer_class = serializers.TaskSerializer
    def get_ndvi(self, image):
        nir = image.select('B5')
        red = image.select('B4')
        return nir.subtract(red).divide(nir.add(red))

    def get(self, request, format=None):
        """
        NDVI Task
        """
        EE_ACCOUNT = credentials.EE_ACCOUNT
        EE_PRIVATE_KEY_FILE =  credentials.EE_PRIVATE_KEY_FILE
        EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)

        ee.Initialize(EE_CREDENTIALS)

        geometry = ee.Geometry.Polygon([[
            [-64.4309949874878,-31.464982360950497],
            [-64.43112373352051,-31.46282263845819],
            [-64.43653106689453,-31.462895850205864],
            [-64.43640232086182,-31.464762730430145],
            [-64.4309949874878,-31.464982360950497],
        ]])

        collection = ee.ImageCollection("LANDSAT/LC8_L1T_TOA").filterDate(datetime.datetime(2012,10,1), datetime.datetime(2017,3,1)).filterBounds(geometry)

        max_ndvi = collection.map(self.get_ndvi).max()
        max_ndvi = max_ndvi.clip(geometry)

        palette = 'FFFFFF,CE7E45,DF923D,F1B555,FCD163,99B718,74A901,66A000,529400,3E8601,207401,056201,004C00,023B01,012E01,011D01,011301'

        opt = {
            "min":.5, 
            "max":1, 
            "palette":palette
        }

        mapid = max_ndvi.getMapId(opt)
        
        info = [{
            "mapid" : mapid["mapid"],
            "token" : mapid["token"],
            "array" : max_ndvi.toArray(),
            "downloadUrl" : str(max_ndvi.getDownloadURL()),
            
        }]
        
        serializer = serializers.TaskSerializer(info, many=True)
        return Response(serializer.data)                
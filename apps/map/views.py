from django.shortcuts import render

import datetime
import ee
import ee.mapclient

def getNDVI(image):
    nir = image.select('B5')
    red = image.select('B4')  
  
    return nir.subtract(red).divide(nir.add(red))

def Init(request):
    
    EE_ACCOUNT = '581556896296-compute@developer.gserviceaccount.com'
    EE_PRIVATE_KEY_FILE = 'ndvi-db45df4e7061.json'
    EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
    
    ee.Initialize(EE_CREDENTIALS)

    geometry = ee.Geometry.Polygon([[
        [-64.4309949874878,-31.464982360950497],
        [-64.43112373352051,-31.46282263845819],
        [-64.43653106689453,-31.462895850205864],
        [-64.43640232086182,-31.464762730430145],
        [-64.4309949874878,-31.464982360950497],
    ]])

    collection = ee.ImageCollection("LANDSAT/LC8_L1T_TOA").filterDate(datetime.datetime(2016,10,1), datetime.datetime(2017,3,1)).filterBounds(geometry)

    maxNDVI = collection.map(getNDVI).max()
    maxNDVI = maxNDVI.clip(geometry)    

    palette = 'FFFFFF,CE7E45,DF923D,F1B555,FCD163,99B718,74A901,66A000,529400,3E8601,207401,056201,004C00,023B01,012E01,011D01,011301'

    opt = {
        "min":.5, 
        "max":1, 
        "palette":palette
    }
    mapid = maxNDVI.getMapId(opt)
    
    template_values = {
        'mapid': mapid['mapid'],
        'token': mapid['token']
    }

    return render(request, 'map/init.html', template_values)    
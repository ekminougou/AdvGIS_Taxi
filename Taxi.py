# Importing libraries
print 'Importing libraries...'
from urllib2 import urlopen
from json import load

key = 'AIzaSyDiyvnT0vQkEoNk7d_wchxWGWMpp9ztacA'
baseUrl = 'https://maps.googleapis.com/maps/api/directions/json?origin='
latOrigin = 40.68813
lonOrigin = -73.95545
latDest = 40.80754
lonDest = -73.96257
limit = 1
#output = open.('Users\markmeiklejohn\Documents\GSAPP\FALL_2015\Advanced_GIS/googleAPIroutes.csv','wb')
##output.write('Name,lat,lon,checkins\n')

# example siteL https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=transit&key=API_KEY

open


# Querying the API
print 'Querying the API...'
request = baseUrl+str(latOrigin)+','+str(lonOrigin)+'&destination='+str(latDest)+','+str(lonDest)+'&mode=transit'+'&departure_time=1343641500'+'&key='+str(key)
print request

response = urlopen(request)
baseData = load(response)
duration=baseData['routes'][0]['legs'][0]['duration']['text']
print duration



print 'done with everything'
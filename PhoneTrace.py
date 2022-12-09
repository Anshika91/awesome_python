import phonenumbers
from test  import number
import opencage
import googlemaps
from datetime import datetime
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))


from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
key = '679f29de89034f5a8783ff823b4d97c1'
geocoder = OpenCageGeocode(key)
query = str(ch_number)
results = geocoder.geocode(query)
print(results)

"""lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)"""



# Create a another file by the name test.py and run it 
number = "+91 xxxxxxxxxx"
# at the place of xxxx write your phone number and dont forget to specify the country code 
# thank you...

import requests

#get the current weather for zipcode 24060
zipcode = '24060'
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=ca4adee6d661b5bfd3ae048f856b07d0')
json_object = r.json()
#get the windspeed
windspeed = float(json_object['wind']['speed'])
print(str(windspeed))
#get the wind direction
wind_direction = float(json_object['wind']['deg'])
print(str(wind_direction))
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#print(r.status_code)
#r.headers['content-type']
#r.encoding
#r.text
#r.json()       #built in json decoder
#r.content       //for non-text requests

#r = requests.get('https://github.com/timeline.json')
#r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')

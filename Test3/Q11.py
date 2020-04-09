import geoip2.database

#reader = geoip2.database.Reader('/home/plymale/violent/GeoLite2-City_20190409 / GeoLite2 - City.mmdb')
#note: for paths, use the "r" at the front to interpret as a raw string. Otherwise your "\"s are interpreted as escapes
reader = geoip2.database.Reader(r"C:\Users\Alex\Documents\School\Semester_8\NetApps_ECE4564\Assignments\Assignment 3\GeoIP2_databases\GeoLite2-City_20190423\GeoLite2-City.mmdb")

response = reader.city('130.208.165.186')

print(response.country.iso_code)
print(response.country.name)
print(response.subdivisions.most_specific.name)
print(response.city.name)
print(response.postal.code)
print(response.location.latitude)
print(response.location.longitude)

reader.close()
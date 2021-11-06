import socket
from ip2geotools.databases.noncommercial import DbIpCity
url=input("enter url \n")
ip=socket.gethostbyname(url)
response=DbIpCity.get(ip,api_key='free')
print("IP",ip)
print(response.city)
print(response.region)
print(response.country)
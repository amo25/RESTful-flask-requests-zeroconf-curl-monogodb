from zeroconf import ServiceInfo, Zeroconf
import socket

desc = {'version':'1.0'}
info = ServiceInfo("_http._tcp.local.", "Team19._http._tcp.local.", socket.inet_aton("127.0.0.1"), 80, 0, 0, desc)
zeroconf = Zeroconf()
zeroconf.register_service(info)
input("Press enter to exit:") #must continue running. If it goes out of scope, service is not longer advertised
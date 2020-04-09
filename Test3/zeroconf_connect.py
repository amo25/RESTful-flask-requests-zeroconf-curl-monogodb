from zeroconf import Zeroconf
import socket

if __name__ == '__main__':
    zeroconf = Zeroconf()
    info = None
    while (info == None): #block until service starts
        info = zeroconf.get_service_info("_http._tcp.local.", "Team19._http._tcp.local.")

    led_address = info.address
    led_ipv4_address = socket.inet_ntoa(led_address)
    led_port = info.port


import RPi.GPIO as GPIO
from zeroconf import Zeroconf, ServiceInfo
from flask import Flask, request, jsonify
import socket

app = Flask(__name__)


def changeLED(status, color, intensity):
    global redpwm,bluepwm,greenpwm,redint,blueint,greenint
    leds['color'] = color
    leds['intensity'] = int(intensity)
    leds['status'] = status
    intens=int(intensity)
    if leds['status'] == 'on':
        if leds['color'] == 'red':
            redint = intens
            greenint = 0
            blueint = 0
        elif leds['color'] == 'blue':
            redint = 0
            greenint = 0
            blueint = intens
        elif leds['color'] == 'green':
            redint = 0
            greenint = intens
            blueint = 0
        elif leds['color'] == 'magenta':
            redint = intens
            greenint = 0
            blueint = intens
        elif leds['color'] == 'cyan':
            redint = 0
            greenint = intens
            blueint = intens
        elif leds['color'] == 'yellow':
            redint = intens
            greenint = intens
            blueint = 0
        elif leds['color'] == 'white':
            redint = intens
            greenint = intens
            blueint = intens
        redpwm.ChangeDutyCycle(redint)
        greenpwm.ChangeDutyCycle(greenint)
        bluepwm.ChangeDutyCycle(blueint)
    else:
        redpwm.ChangeDutyCycle(0)
        greenpwm.ChangeDutyCycle(0)
        bluepwm.ChangeDutyCycle(0)

@app.route('/LED', methods=['POST'])
def led_post():
    #print(request.args)
    status = request.args.get('status')
    color = request.args.get('color')
    intensity = request.args.get('intensity')
    changeLED(status,color,intensity)
    return ''

@app.route('/LED', methods=['GET'])
def led_get():
    try:
        response = jsonify(leds)
        response.status_code = 200
    except :
        return Response('Data could not be accessed', 400)
    return response

def ad():
    desc = {'version':'1.0'}  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 7777))
    ip = s.getsockname()[0]
    s.close()
    info = ServiceInfo("_http._tcp.local.",
                   "_led._http._tcp.local.",
                   socket.inet_aton(ip), 7777, 0, 0,
                   desc)
    Zeroconf().register_service(info)

#GPIO setup
channels=[16,20,21]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels,GPIO.OUT)

redpwm = GPIO.PWM(16, 100)
greenpwm = GPIO.PWM(20, 100)
bluepwm = GPIO.PWM(21, 100)

redpwm.start(0)
greenpwm.start(0)
bluepwm.start(0)

redint = 0
blueint = 0
greenint = 0
leds = {'color':'none',
        'intensity':'none',
        'status':'none'}
ad()
app.run(host='0.0.0.0',port=7777,debug=True)
    

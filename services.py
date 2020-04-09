import sys
from functools import wraps
from pymongo import MongoClient
from flask import request, Response, Flask, send_file
from servicesKeys import *
from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange
import socket
from time import sleep
import requests
import os

app = Flask(__name__)

def check_auth(username, password):
    user = collection.find_one({'username': username})
    ret = False
    if user['password'] == password:
        ret = True
    return ret

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
    
@app.route('/goodbye')
@requires_auth
def goodbye_world():
    return "Goodbye World\n"

@app.route('/Canvas', methods=['GET'])
@requires_auth
def canvas_download():
    file = request.args.get('file')
    try:
        url = 'https://vt.instructure.com/api/v1/courses/83639/files/?access_token='+canvas_key
        r = requests.get(url)
        json_info = r.json()
        print(json_info)
        for item in json_info:
            if item['filename'] == file:
                theid = item['id']
        url = 'https://vt.instructure.com/api/v1/courses/83639/files/'+str(theid)+'?access_token='+canvas_key
        r = requests.get(url, allow_redirects=True)

        file_path = os.getcwd() + os.sep + file
        with open(file_path, 'wb') as f:
            f.write(r.content)
    except:
        return Response('Error', 500)

    return send_file(file)

@app.route('/LED', methods = ['POST'])
@requires_auth
def post_led():
    info = Zeroconf().get_service_info('_http._tcp.local.', '_led._http._tcp.local.')
    address = socket.inet_ntoa(info.address)
    port = info.port
    if info is None:
        return Response('Service Unavailable', 503)

    url = "http://"+address+':'+str(port)+"/LED"
    return requests.post(url, params=request.args).text

@app.route('/LED', methods = ['GET'])
@requires_auth
def get_led():
    info = Zeroconf().get_service_info('_http._tcp.local.', '_led._http._tcp.local.')
    address = socket.inet_ntoa(info.address)
    port = info.port
    if info is None:
        return Response('Service Unavailable', 503)
    url = "http://"+address+':'+str(port)+"/LED"
    return requests.get(url).text

client = MongoClient()
db = client['db']
collection = db.users
collection.insert_one({'username': 'Admin', 'password': 'pass'})
collection.insert_one({'username': 'Maura', 'password': 'maura_pass'})
collection.insert_one({'username': 'Mark', 'password': 'mark_pass'})
collection.insert_one({'username': 'Alex', 'password': 'alex_pass'})

app.run(host='0.0.0.0',port=8080,debug=True)

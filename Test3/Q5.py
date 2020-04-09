from functools import wraps
from flask import Flask, request, Response
import string

app = Flask(__name__)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'Silver' and password == 'Surfer'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

#@app.route("/")
#@requires_auth
#def hello():
    #return "Hello World!\n"

@app.route('/reverse/<string:original_string>')
@requires_auth
def reverse(original_string):
    reversed = original_string[::-1]
    return reversed

@app.route('/length/<string:original_string>')
@requires_auth
def length(original_string):
    length = len(original_string)
    return str(length)

@app.route('/upcase/<string:original_string>')
@requires_auth
def upcase(original_string):
    upcase = original_string.upper()
    return upcase

@app.route('/sort_str/<string:original_string>')
@requires_auth
def sort_str(original_string):
    sortedM = ''.join(sorted(original_string))
    return sortedM

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
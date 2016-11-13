from bottle import Bottle, run, response, request
#from routes import *

app = Bottle()


@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route("/techs", method=['OPTIONS', 'GET'])
def techs():
    if request.method == 'OPTIONS':
        return {}
    return {'techs': [{'name': 'python'},{'name': 'django'},{'name': 'nodejs'}]}


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000, debug=True, reloader=True)

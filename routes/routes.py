import settings
from db_settings import session
from bottle import route, view, static_file, url

@route("/")
@view("index")
def index():
    return { "get_url": url }

@route("/tech/<id:int>", name="tech")
@view("tech")
def tech(id):
    return { "get_url": url }

@route("/quotes")
@view("quotes")
def quotes():
    return { "get_url": url }

@route("/gallery")
@view("gallery")
def gallery():
    return { "get_url": url }

@route("/images/<filename:re:.*\.*>", name="images")
def get_image(filename):
    return static_file(filename, root="static/img/", mimetype="image/jpeg")

@route("/static/<filename:path>", name="static")
def static(filename):
    return static_file(filename, root=settings.BASE_DIR+"/static/")

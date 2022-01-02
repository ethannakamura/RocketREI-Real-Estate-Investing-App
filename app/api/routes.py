from flask import Blueprint

api = Blueprint('api', __name__,url_prefix='/api')

@api.route('/')
def apidata():
    return {'datadtadata': 'ook look at this fancy data'}
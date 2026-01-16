from flask import Blueprint


user = Blueprint('usuariobp', __name__, url_prefix='/usuario', template_folder='templates', static_folder='./static/')


from .rotas import *


from flask import Blueprint


auth = Blueprint('authbp',__name__, url_prefix="/auth",template_folder="templates", static_folder="./static/")


from .rotas import *


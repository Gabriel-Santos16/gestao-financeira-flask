from flask import Blueprint



main = Blueprint('mainbp',__name__, template_folder="templates", static_folder="staticMain")

from .rotas import *
    
   
                           
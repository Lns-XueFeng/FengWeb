from flask import Blueprint


api_bp = Blueprint("apis", __name__)


from .links import *
from .messages import *
from .notes import *
from .posts import *

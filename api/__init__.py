from flask import Blueprint
from .meme import meme_bp

master_blueprint = Blueprint('main', __name__, url_prefix='/api')

master_blueprint.register_blueprint(meme_bp)

@master_blueprint.route('/')
def home():
    return "This is API's route!"

import os
import importlib
from flask import Blueprint

meme_bp = Blueprint('meme', __name__, url_prefix='/meme')
current_dir = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(current_dir):
    if filename == '__init__.py' or not filename.endswith('.py'):
        continue
    module_name = filename[:-3]
    module = importlib.import_module(f'.{module_name}', package=__name__)
    meme_bp.add_url_rule(f'/{module_name}', view_func=getattr(module, module_name), methods=['GET', 'POST'])
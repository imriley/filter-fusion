import os
import importlib
from flask import Blueprint

meme_bp = Blueprint('meme', __name__, url_prefix='/api/meme')

# Get the directory containing this file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Iterate over the files in the directory
for filename in os.listdir(current_dir):
    # Skip __init__.py and non-Python files
    if filename == '__init__.py' or not filename.endswith('.py'):
        continue

    # Get the module name by removing the .py extension
    module_name = filename[:-3]

    # Import the module
    module = importlib.import_module(f'.{module_name}', package=__name__)

    # Register the route with the blueprint
    meme_bp.add_url_rule(f'/{module_name}', view_func=getattr(module, module_name))
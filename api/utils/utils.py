import re
import requests
from io import BytesIO
from PIL import Image
from flask import request
from pathlib import Path
from api.utils.errors import NoImageProvided, InvalidImageUrl

def get_template(name: str) -> Image:
    """
    Retrieves a template image given its name.

    Parameters:
        name (str): The name of the template image.

    Returns:
        Image: The template image in RGBA format.
    """
    ASSET = Path(__file__).parent.parent / 'assets' / 'meme templates'
    return Image.open(ASSET / f'{name}.png', mode='r').convert('RGBA')

def get_image() -> Image:
    """
    Retrieves an image from either a file upload or a URL.

    Returns:
        Image: The retrieved image.

    Raises:
        InvalidImageUrl: If the provided URL is invalid.
        NoImageProvided: If neither a file upload nor a URL is provided.
    """
    if image_file := request.files.get('image'):
        return Image.open(image_file)
    if image_url := request.form.get('image_url'):
        if match := re.match(r"(?:http\:|https\:)?\/\/.*\.(?:png|jpg|webp|jpeg)", image_url):
            image_file = requests.get(match.group())
            return Image.open(BytesIO(image_file.content))
        raise InvalidImageUrl
    raise NoImageProvided
        
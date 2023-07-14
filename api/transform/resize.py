from PIL import Image
from io import BytesIO
from flask import send_file, abort, request
from api.utils.utils import get_image


def resize():
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))

    if width is None or height is None:
        abort(400, 'Width and height parameters are required.')
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))
    
    resized_image = image.resize((height, width), Image.LANCZOS)
    resized_image_file = BytesIO()
    resized_image.save(resized_image_file, "PNG")
    resized_image_file.seek(0)
    resized_image.close()
    return send_file(resized_image_file, mimetype='image/png')

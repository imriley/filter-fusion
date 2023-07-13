from io import BytesIO
from PIL import Image
from flask import send_file, abort
from api.utils.utils import get_image


def grayscale():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))
    grayscale_image = image.convert("L")
    img_bytes = BytesIO()
    grayscale_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Send the grayscale image as a response
    return send_file(img_bytes, mimetype="image/png")

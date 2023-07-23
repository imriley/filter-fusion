from io import BytesIO
from PIL import ImageOps, Image
from flask import send_file, abort
from api.utils.utils import get_image

fill_white = (255, 255, 255)


def invert():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))

    if image.mode != "RGB":
        image = image.convert("RGB")
    inverted = ImageOps.invert(image)
    img_bytes = BytesIO()
    inverted.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return send_file(img_bytes, mimetype="image/png")

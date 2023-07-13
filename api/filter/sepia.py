from io import BytesIO
from PIL import ImageOps
from flask import send_file, abort
from api.utils.utils import get_image


def sepia():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))

    # Convert image to grayscale
    grayscale_image = image.convert("L")

    # Apply sepia filter using ImageOps.colorize
    sepia_image = ImageOps.colorize(grayscale_image, "#704214", "#C0A375")

    img_bytes = BytesIO()
    sepia_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # Send the sepia image as a response
    return send_file(img_bytes, mimetype="image/png")

from io import BytesIO
from PIL import Image
from flask import abort, send_file
from api.utils.utils import get_image, get_template

def feelings():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, exc)
    template = get_template('mensfeeling')
    new = Image.new("RGBA", template.size, None)
    image = image.resize((300, 300))
    new.paste(template)
    new.paste(image, (75, 520))
    fp = BytesIO()
    new.save(fp, "PNG")
    fp.seek(0)
    new.close()
    image.close()
    template.close()
    return send_file(fp, mimetype='image/png')
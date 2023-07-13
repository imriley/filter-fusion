from io import BytesIO
from PIL import Image
from flask import send_file, abort
from api.utils.utils import get_image, get_template

def bonk():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))
    template = get_template('bonk')
    im = Image.new("RGBA", template.size)
    head = image.resize((200, 200), Image.LANCZOS)
    im.paste(head, (425, 235))
    im.paste(template, mask=template)
    fp = BytesIO()
    im.save(fp, "PNG")
    fp.seek(0)
    im.close()
    return send_file(fp, mimetype='image/png')
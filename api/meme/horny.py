from io import BytesIO
from PIL import Image
from flask import send_file, abort
from api.utils.utils import get_image, get_template

def horny():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))
    im = Image.new("RGBA", (360, 300), None)
    template = get_template('horny')
    image = image.resize((85, 85))
    image = image.rotate(angle=22, resample=Image.LANCZOS, expand=True)
    im.paste(image, (0, 0), template)
    template.close()
    fp = BytesIO()
    im.save(fp, "PNG")
    fp.seek(0)
    im.close()
    return send_file(fp, mimetype='image/png')
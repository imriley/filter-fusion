from io import BytesIO
from PIL import Image
from flask import send_file, abort
from api.utils.utils import get_image, get_template

def simp():
    try:
        image = get_image()
    except Exception as exc:
        abort(400, str(exc))
    im = Image.new("RGBA", (500, 319), None)
    template = get_template("simp")
    image = image.resize((136, 136), Image.LANCZOS)
    image = image.rotate(angle=3, resample=Image.BILINEAR, expand=True)
    im.paste(image, (73, 105))
    image.close()
    im.paste(template, (0, 0), template)
    template.close()
    fp = BytesIO()
    im.save(fp, format="PNG")
    fp.seek(0)
    im.close()
    return send_file(fp, mimetype="image/png")

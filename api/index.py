from flask import Flask, redirect
from meme import meme_bp

app = Flask(__name__)

app.register_blueprint(meme_bp)

@app.route('/')
def home():
    return redirect('https://github.com/imriley/filter-fusion/blob/main/README.md')

# if __name__ == '__main__':
#     app.run()
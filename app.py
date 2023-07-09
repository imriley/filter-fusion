from flask import Flask, redirect
from api import master_blueprint

app = Flask(__name__)

app.register_blueprint(master_blueprint)

@app.route('/')
def home():
    return redirect('https://github.com/imriley/filter-fusion/blob/main/README.md')

@app.errorhandler(404)
def page_not_found(error):
    return error, 404

if __name__ == '__main__':
    app.run()
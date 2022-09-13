from flask import Blueprint
from flask import Flask, render_template

caster = Blueprint('caster', __name__, url_prefix='/')


def create_app():
    app = Flask(__name__)
    app.register_blueprint(caster)
    return app


@caster.route("/")
def display1():
    return render_template('demo.html')

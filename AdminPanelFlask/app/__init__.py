from flask import Flask , render_template
app = Flask(__name__)

from .login.controller import login
app.register_blueprint(login)
import os
from flask import Flask
import auth, mailing_list, embed

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)
app.config.from_pyfile('config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(auth.bp)
app.register_blueprint(mailing_list.bp)
app.register_blueprint(embed.bp)

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'
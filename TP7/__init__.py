from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

scss = Bundle('scss/index.scss', filters='libsass', output='css/index.css')
assets.register('scss_all', scss)

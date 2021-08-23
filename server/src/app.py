from flask import Flask
from env import isProd

app = Flask(__name__, static_folder='../client/build', static_url_path='/') if isProd() else Flask(__name__)
app.secret_key = 'earle'
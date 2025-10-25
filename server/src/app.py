import os
from flask import Flask
from env import isProd

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__, static_folder='../client/build', static_url_path='/') if isProd() else Flask(__name__)
app.secret_key = 'earle'

print('Prod' if isProd() else "Not prod")
from flask import Flask, render_template
# import extensions
import controllers
from utils import config
import sys

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')


# Register the controllers
# app.register_blueprint(controllers.album)
# app.register_blueprint(controllers.albums)
# app.register_blueprint(controllers.pic)
app.register_blueprint(controllers.main)
app.secret_key = 'autocaption'


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
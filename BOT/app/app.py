from flask import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

def login_view():
    pass

def signup_view():
    pass

if __name__ == "__main__":
    app.run(port = 8087)
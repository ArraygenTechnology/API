from .. import app

@app.route("/")
def login_page():
    return "<h1>login page</h1>"
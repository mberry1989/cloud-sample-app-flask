from flask import Flask, render_template
from DancingGoat.views.home import home
from DancingGoat.views.articles import articles

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(articles)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_pages/404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error_pages/500.html')

app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_server_error)

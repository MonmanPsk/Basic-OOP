from flask import Flask, render_template
from flask.views import MethodView #MethodView = class

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("home_page.html")

app.add_url_rule("/", view_func=HomePage.as_view("Home"))

if __name__ == "__main__":
    app.run()
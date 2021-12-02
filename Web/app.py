from flask import Flask, render_template, request
from flask.views import MethodView #MethodView = class
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("home_page.html")

class BillForm(Form):
    amount = StringField("Enter amount : ")
    period = StringField("Enter period : ")

    button = SubmitField("Submit")

class InputPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("input_page.html", bill_form = bill_form)

class ResultPage(MethodView):
    def post(self):
        form = BillForm(request.form)
        amount = form.amount.data
        period = form.period.data

        return f"{amount} {period}"

app.add_url_rule("/", view_func=HomePage.as_view("Home"))
app.add_url_rule("/form", view_func=InputPage.as_view("form"))
app.add_url_rule("/result", view_func=ResultPage.as_view("result"))

if __name__ == "__main__":
    app.run()
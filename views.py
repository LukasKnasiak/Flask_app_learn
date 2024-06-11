from flask import Flask, render_template, Blueprint

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/myname")
def myname():
    my_name = "Lukas"
    return render_template("myname.html", my_name = my_name)


@my_view.route("/countries")
def countries():
    return render_template("countries.html")


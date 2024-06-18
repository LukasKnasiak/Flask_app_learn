from flask import Blueprint, render_template, request
from fav_countries import favourite_countries, favourite_capitols, favourite_cities, favourite_continent, favourite_ratings

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html", favourite_countries=favourite_countries,
                           favourite_continent=favourite_continent,
                           favourite_capitols=favourite_capitols,
                           favourite_cities=favourite_cities,
                           ratings=favourite_ratings)

@my_view.route("/myname", methods=["GET", "POST"])
def myname():
    if request.method == "POST":
        new_country = request.form.get("added_country")
        if new_country:
            favourite_countries.append(new_country)

        new_continent = request.form.get("added_continent")
        if new_continent:
            favourite_continent.append(new_continent)

        new_capitol = request.form.get("added_capitol")
        if new_capitol:
            favourite_capitols.append(new_capitol)

        new_city = request.form.get("added_city")
        if new_city:
            favourite_cities.append(new_city)

        rating = request.form.get("rating")
        if rating is not None:
            rating = int(rating)
            favourite_ratings.append(rating)

    return render_template("myname.html")

@my_view.route("/countries")
def countries():
    return render_template("countries.html")

@my_view.route("/filter")
def filter():
    return render_template("filter.html")

@my_view.route("/filtered_countries", methods=["POST"])
def filtered_countries():
    if request.method == "POST":
        rating = request.form.get("rating")
        if rating:
            rating = int(rating)
            filtered_data = [(country, continent, capital, city, stars) for country, continent, capital, city, stars in zip(favourite_countries, favourite_continent, favourite_capitols, favourite_cities, favourite_ratings) if stars == rating]
        else:
            filtered_data = [] 

        return render_template("filtered_countries.html", filtered_data=filtered_data)

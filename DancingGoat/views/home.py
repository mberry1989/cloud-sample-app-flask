import requests
import datetime
from flask import render_template, Blueprint, current_app as app
from DancingGoat.helpers.type import TypeHelper
from DancingGoat.models import Home, HeroUnit, Article

home = Blueprint("home",__name__)

@home.route("/")
def index():
    # possibly separate into a repo.
    r = requests.get("https://deliver.kenticocloud.com/{}/items/home".format(app.config["KC_PROJECT_ID"]))
    r.raise_for_status()

    r = r.json()

    if r["item"]:
        elements = r["item"]["elements"]
        modular = r["modular_content"]
        contact_info = elements["contact"]["value"]
        home_hero_unit = {}
        home_articles = {}
        if modular:
            for item, value in modular.items():
                if item in elements["hero_unit"]["value"]:                
                    home_hero_unit[item] = TypeHelper.parse_json("hero_unit", value)
                if item in elements["articles"]["value"]:
                    home_articles[item] = TypeHelper.parse_json("article", value)

        home = Home(home_hero_unit,home_articles, contact_info)
        
        return render_template("index.html",contact=home.contact, hero_unit=home.hero_unit, articles= home.articles, time=datetime.datetime.utcnow().strftime("%Y"))
    return render_template("error_pages/404.html"), 404

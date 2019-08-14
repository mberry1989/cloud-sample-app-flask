import requests
from flask import render_template, Blueprint, current_app as app
from DancingGoat.helpers.type import TypeHelper
from DancingGoat.resolvers.inline_resolver import InlineResolver

articles = Blueprint("articles",__name__)

@articles.route("/articles")
def index():
        r = requests.get("https://deliver.kenticocloud.com/{}/items?system.type=article&order=elements.post_date[desc]".format(app.config["KC_PROJECT_ID"]))
        r.raise_for_status()

        r = r.json()

        if r["items"]:
                value = r["items"]
                article_list = []
                for article in value:
                        article = TypeHelper.parse_json("article", article)
                        article_list.append(article)
                return render_template("articles.html",articles=article_list)
        return render_template("error_pages/404.html"), 404
        

@articles.route("/articles/<url_pattern>")
def show(url_pattern):        
        r = requests.get("https://deliver.kenticocloud.com/{}/items?system.type=article&elements.url_pattern={}".format(app.config["KC_PROJECT_ID"], url_pattern))
        r.raise_for_status()

        r = r.json()

        if r["items"]:
                value = r["items"][0]
                article = TypeHelper.parse_json("article", value)
                related_articles = []
                if len(r["modular_content"]) > 0:
                        # Resolve inline content items for Rich Text Elements
                        modular = r["modular_content"]
                        resolved_content = InlineResolver.resolve_inline_items(str(article.body_copy), modular)
                        article.body_copy = resolved_content
                        # Handle related articles
                        for key, value in modular.items():
                                if key in article.related_articles:
                                        related_article = TypeHelper.parse_json("article", value)
                                        related_articles.append(related_article)
                # Resolve inline content item links for rich Text Elements
                if len(article.inline_links) > 0:
                        resolved_content = InlineResolver.resolve_inline_links(str(article.body_copy), article.inline_links)
                        article.body_copy = resolved_content

                return render_template("article.html",article=article, related_articles=related_articles)
        return render_template("error_pages/404.html"), 404
    

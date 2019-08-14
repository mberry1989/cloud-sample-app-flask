import datetime

class Article():
    def __init__(self, title, teaser_image, post_date, summary, body_copy, inline_links, related_articles, meta_keywords, personas, meta_description, url_pattern, sitemap):
        self.title = title
        self.teaser_image = teaser_image
        self.post_date = datetime.datetime.strptime(post_date, "%Y-%m-%dT%H:%M:%SZ")
        self.summary = summary
        self.body_copy = body_copy
        self.inline_links = inline_links
        self.related_articles = related_articles
        self.meta_keywords = meta_keywords
        self.personas = personas
        self.meta_description = meta_description
        self.url_pattern = url_pattern
        self.sitemap = sitemap

class HeroUnit():
    def __init__(self, title, image, marketing_message, sitemap):
        self.title = title
        self.image = image
        self.marketing_message = marketing_message
        self.sitemap = sitemap

class Home():
    def __init__(self, hero_unit, articles, contact):
        self.hero_unit = hero_unit
        self.articles = articles
        self.contact = contact

class Tweet():
    def __init__(self, tweet_link, theme, display_options):
        self.tweet_link = tweet_link
        self.theme = theme 
        self.display_options = display_options

class Video():
    def __init__(self, video_id, video_host):
        self.video_id = video_id
        self.video_host = video_host


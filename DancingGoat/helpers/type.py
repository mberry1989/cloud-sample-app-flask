from DancingGoat.models import Home, HeroUnit, Article, Tweet, Video

class TypeHelper():
    def parse_json(content_type, value):
        if content_type == "article":
            item = Article(
            value["elements"]["title"]["value"], 
            value["elements"]["teaser_image"]["value"],
            value["elements"]["post_date"]["value"], 
            value["elements"]["summary"]["value"],
            value["elements"]["body_copy"]["value"],
            value["elements"]["body_copy"]["links"], 
            value["elements"]["related_articles"]["value"],
            value["elements"]["meta_keywords"]["value"], 
            value["elements"]["personas"]["value"],
            value["elements"]["meta_description"]["value"],
            value["elements"]["url_pattern"]["value"], 
            value["elements"]["sitemap"]["value"])
        
        elif content_type == "hero_unit":
            item = HeroUnit(
            value["elements"]["title"]["value"], 
            value["elements"]["image"]["value"], 
            value["elements"]["marketing_message"]["value"], 
            value["elements"]["sitemap"]["value"])

        elif content_type == "tweet":
            item = Tweet(
            value["elements"]["tweet_link"]["value"], 
            value["elements"]["theme"]["value"],
            value["elements"]["display_options"]["value"])

        elif content_type == "hosted_video":
            item = Video(
            value["elements"]["video_id"]["value"], 
            value["elements"]["video_host"]["value"])

        return item
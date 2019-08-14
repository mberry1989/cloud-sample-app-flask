from DancingGoat.helpers.type import TypeHelper
from bs4 import BeautifulSoup, Tag

class InlineResolver():
    def resolve_inline_items(content, modular_content):
        soup = BeautifulSoup(content, features="html.parser")

        # Inline Linked item resolution for Tweets, YouTube Videos, Articles
        for key, value in modular_content.items(): 
            obj = soup.find("object", attrs={"data-codename":key})
            if obj:      
                if value["system"]["type"] == "tweet":
                    tweet = TypeHelper.parse_json("tweet", value)
                    new_tag = BeautifulSoup("<blockquote class=\"twitter-tweet\" data-lang=\"en\" data-theme=\"{}\"><a href=\"{}\"></a></blockquote>".format(tweet.theme[0]["codename"], tweet.tweet_link),features="html.parser")
                    obj.replaceWith(new_tag)
                    if not soup.find("script", attrs={"async src":"https://platform.twitter.com/widgets.js"}):
                        widget_tag = soup.new_tag("script", attrs={"async":None,"src": "https://platform.twitter.com/widgets.js", "charset":"utf-8"})
                        soup.append(widget_tag)

                elif value["system"]["type"] == "hosted_video":
                    video = TypeHelper.parse_json("hosted_video", value)
                    new_tag = BeautifulSoup("<div><iframe type=\"text/html\" width=\"640\" height=\"385\" style=\"display:block; margin: auto; margin-top:30px ; margin-bottom: 30px\" src=\"https://www.youtube.com/embed/{}?autoplay=1\" frameborder=\"0\"></iframe></div>".format(video.video_id),features="html.parser")
                    obj.replaceWith(new_tag)

                elif value["system"]["type"] == "article":
                    article = TypeHelper.parse_json("article", value)
                    new_tag = BeautifulSoup("<a href='/articles/{}'>{}</a> ".format(article.url_pattern, article.title),features="html.parser")
                    obj.replaceWith(new_tag)
        return soup

    # Inline link resolution for Content Items
    def resolve_inline_links(content, inline_links):
        print(inline_links)
        soup = BeautifulSoup(content)
            
        for key, value in inline_links.items():
            print(value) 
            obj = soup.find("a", attrs={"data-item-id":key})
            if obj:   
                obj["href"] = "/{}/{}".format(value["type"],value["url_slug"])
        return soup
        
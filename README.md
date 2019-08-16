# cloud-sample-app-flask
The Dancing Goat demo site created using Flask and Jinja2 templates without an SDK and beginner-level knowledge of Python and Flask.

This application is meant for use with the Dancing Goat sample project within Kentico Cloud. The project contains the home page and article content for Dancing Goat – an imaginary chain of coffee shops. If you don't have your own Sample Project, any administrator of a Kentico Cloud subscription [can generate one](https://app.kenticocloud.com/sample-project-generator).

### Setup

1. Clone the repository
2. Open the [config.py](/config.py) file and set the KC_PROJECT_ID variable to your sample project's Project ID:
3. Run the following commands:
```
pip install -r requirements.txt
app.py
```
The application will then be available at localhost:5000 .

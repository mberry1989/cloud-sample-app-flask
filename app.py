from DancingGoat import app

app.config.from_object('config.DefaultConfig')

if __name__ == '__main__':
    app.run(debug=False)
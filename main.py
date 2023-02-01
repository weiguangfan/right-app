from flask import Flask
from home import home_blue

app = Flask(__name__)

app.register_blueprint(home_blue)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)








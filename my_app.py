from flask import Flask
import imgVision


app = Flask(__name__)

@app.route("/")
def home_page():
    plate = imgVision.run_quickstart()
    return plate

if __name__ == '__main__':
    app.run(port=80)
from flask import Flask
import imgVision
import requests

#HTTP Resquest with plate
def passLicensePlate(licensePlate):
    url = "http://e760bbea3267.ngrok.io/notify/" + licensePlate
    r = requests.get(url)


app = Flask(__name__)

@app.route("/")
def home_page():
    plate = imgVision.run_quickstart()
    return plate

if __name__ == '__main__':
    plate = imgVision.run_quickstart()
    passLicensePlate(plate)
    app.run(port=80)

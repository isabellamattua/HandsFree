from flask import Flask
import imgVision
import requests


def passLicensePlate(licensePlate):
    payload = {'licensePlate':licensePlate}
    r = requests.get()


app = Flask(__name__)

@app.route("/")
def home_page():
    plate = imgVision.run_quickstart()
    return plate

if __name__ == '__main__':
    app.run(port=80)
    plate = imgVision.run_quickstart()

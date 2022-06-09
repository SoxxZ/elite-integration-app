import json
from flask import Flask



app = Flask(__name__)

with open("Status.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

@app.route('/data')
def hello():
    return jsonObject

app.run(host="127.0.0.1", port=1722)



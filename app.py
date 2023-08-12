from flask import Flask, jsonify, request
from selectedRec import selected_rec
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/getColums", methods=["POST"])
def getCoumns():
    data = request.json
    print(data["data"])
    response = selected_rec(data["data"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
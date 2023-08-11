from flask import Flask, jsonify, request
from selectedRec import selected_rec
app = Flask(__name__)


@app.route("/getColums", methods=["POST"])
def getCoumns():
    data = request.json
    print(data["data"])
    response = selected_rec(data["data"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
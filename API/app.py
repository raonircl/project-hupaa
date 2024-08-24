from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/v1/", methods=["GET"])
async def say_hello():
    return jsonify({"message": "hello!"})

if __name__=="__main__":
    app.run(debug=True)
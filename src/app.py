from flask import Flask, request, jsonify, render_template
from db import find_person

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    name = request.args.get("name", "").strip()
    if not name:
        return jsonify({"results": [], "error": "이름을 입력해주세요."})

    results = find_person(name)

    if not results:
        return jsonify({"results": [], "error": f"'{name}' 을(를) 찾을 수 없습니다."})

    return jsonify({"results": results, "error": None})


if __name__ == "__main__":
    app.run(debug=True)
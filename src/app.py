import os
from flask import Flask, request, jsonify, render_template
from db import find_person
from init_db import init  # ← 추가

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

init()  # ← 앱 시작할 때 DB 초기화

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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
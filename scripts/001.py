# /// script
# dependencies = [
#   "flask"
# ]
# ///

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "我就是一個網頁囉！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
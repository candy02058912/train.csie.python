# /// script
# dependencies = [
#   "flask"
# ]
# ///

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "歡迎來上 Candy 的 Python 課！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
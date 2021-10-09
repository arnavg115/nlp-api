
from flask import Flask, request, jsonify
import transformers


summarizer = transformers.pipeline("summarization")



app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
   json:dict = request.get_json(force=True)
   text = json.get("text")
   res = summarizer(text,min_length=30,max_length=100) if text != None else {"error":True}
   return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
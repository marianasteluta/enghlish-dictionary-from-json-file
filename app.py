from flask import Flask, request, render_template
import json
import difflib

app = Flask(__name__)


def format_definition(s):
    s = s.replace("1. ", "\n1. ")
    return s


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    with open(r'static\dictionary.json', 'r') as f:
        words_data = json.load(f)
    word = ""
    definition = ""
    words_close = []
    if request.method == 'POST' and 'word' in request.form:
        word = request.form.get("word")
        word = word.lower()
        word = word.strip()

    for a in words_data:
        if a == word:
            definition = words_data[a]

    if definition == "":
        words_close = difflib.get_close_matches(word, words_data.keys())

    return render_template('index.html', word=word, definition=format_definition(definition), words_close=words_close)


if __name__ == '__main__':
    app.run(debug=True)

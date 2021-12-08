import os

from flask import Flask, render_template, request 
from match import match

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route("/")
def start():
    title = "Dictionary"
    
    text = """"""

    choices = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        choices.append(letter)
    print(choices)

    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/letter")
def words():
    letter = request.args.get('letter').upper()
    match_middle = request.args.get('match_middle')
    anywhere = request.args.get('anywhere')

    title = letter + " words"
    
    text = """"""

    choices = []
    a_file = open("words.txt")

    lines = a_file.read().splitlines()
    
    for line in lines:
        if anywhere:
            if match(letter, line):
                choices.append(line)
        elif match_middle:
            if  letter in line:
                choices.append(line)
        else:
            if  line.startswith(letter):
                choices.append(line)

    return render_template('words.html', title=title, text=text, choices=choices)

app.run(host='0.0.0.0', port=port, debug=True)

import os

from flask import Flask, render_template, request 

app = Flask(__name__)


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
    letter = request.args.get('letter')
    match_middle = request.args.get('match_middle')
    anywhere = request.args.get('anywhere')

    title = letter + " words"
    
    text = """"""

    choices = []
    a_file = open("words.txt")

    lines = a_file.read().splitlines()
    print(match_middle, anywhere)
    for line in lines:
        if anywhere:
            if "".join(sorted(letter)) in "".join(sorted(line)):
                choices.append(line)
        elif match_middle:
            if  letter in line:
                choices.append(line)
        else:
            if  line.startswith(letter):
                choices.append(line)

    return render_template('words.html', title=title, text=text, choices=choices)


# app.py
from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'rockpaperscissorssecret'

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    you_choice = None
    computer_choice = None

    if request.method == "POST":
        youstr = request.form.get("choice")
        youDict = {"s": 1, "p": -1, "c": 0}
        
        reversedict = {1: "Stone 🪨", -1: "Paper 📄", 0: "Scissor ✂️"}

        if youstr in youDict:
            you = youDict[youstr]
            computer = random.choice([-1, 0, 1])

            you_choice = reversedict[you]
            computer_choice = reversedict[computer]

            if computer == you:
                result = "It's a Draw!"
            elif (computer == -1 and you == 0) or \
                 (computer == 0 and you == 1) or \
                 (computer == 1 and you == -1):
                result = "You Win!"
            else:
                result = "You Lose!"
        else:
            result = "Invalid Input!"

    return render_template("index.html", result=result, you_choice=you_choice, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
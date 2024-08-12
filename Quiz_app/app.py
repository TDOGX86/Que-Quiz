from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('question_bank.json', 'r') as file:
    questions = json.load(file)["questions"]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    score = 0
    for q in questions:
        if q["answer"] == data.get(q["question"]):
            score += 1
    return jsonify({"score": score, "total": len(questions)})

if __name__ == '__main__':
    app.run(debug=True)

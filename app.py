from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

all_questions = [
    {
        "id": 1,
        "question": "What number comes next in the sequence? 2, 4, 8, 16, ?",
        "options": ["18", "20", "32", "24"],
        "answer": "32"
    },
    {
        "id": 2,
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
        "options": ["Yes", "No", "Cannot say", "Only sometimes"],
        "answer": "Yes"
    },
    {
        "id": 3,
        "question": "Which shape completes the pattern? △ ○ △ ○ △ ?",
        "options": ["○", "△", "□", "◇"],
        "answer": "○"
    },
    {
        "id": 4,
        "question": "Find the odd one out: Apple, Banana, Carrot, Mango",
        "options": ["Banana", "Carrot", "Mango", "Apple"],
        "answer": "Carrot"
    },
    {
        "id": 5,
        "question": "If you rearrange the letters 'LNGEDNA', what word do you get?",
        "options": ["Gandlen", "England", "Angelnd", "Ladgen"],
        "answer": "England"
    },
    {
        "id": 6,
        "question": "What comes next? Monday, Wednesday, Friday, ?",
        "options": ["Saturday", "Sunday", "Tuesday", "Thursday"],
        "answer": "Sunday"
    }
]

@app.route('/')
def home():
    questions = random.sample(all_questions, 3)
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    answers = data.get('answers', {})
    score = 0
    total = len(answers)

    submitted_questions = [q for q in all_questions if str(q['id']) in answers]

    for q in submitted_questions:
        qid = str(q['id'])
        if qid in answers and answers[qid] == q['answer']:
            score += 1

    percent = (score / total) * 100 if total else 0

    if percent == 100:
        result = "Genius IQ! 🌟"
    elif percent >= 70:
        result = "Above Average IQ 👍"
    elif percent >= 40:
        result = "Average IQ 🙂"
    else:
        result = "Needs Improvement 🤔"

    return jsonify({'score': score, 'total': total, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)

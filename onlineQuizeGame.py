from flask import Flask, jsonify, request
# Inside your Flask app file
from flask import render_template

from onlineQuizGame import app


@app.route('/quizzes/html', methods=['GET'])
def get_quizzes_html():
    return render_template('quizzes.html', quizzes=quizzes)

app = Flask(__name__)

# Sample data for quizzes and users
quizzes = [
    {"id": 1, "title": "Sample Quiz 1", "questions": [...]},
    {"id": 2, "title": "Sample Quiz 2", "questions": [...]},
    # More quizzes...
]

users = [
    {"id": 1, "username": "user1", "quizzes_taken": [1], "score": 85},
    {"id": 2, "username": "user2", "quizzes_taken": [2], "score": 92},
    # More users...
]


# Routes for quizzes
@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify(quizzes)


@app.route('/quiz/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz = next((q for q in quizzes if q["id"] == quiz_id), None)
    if quiz:
        return jsonify(quiz)
    return jsonify({"message": "Quiz not found"}), 404


# Routes for user profiles
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404


# Add more routes for creating quizzes, taking quizzes, user authentication, etc.

if __name__ == '__main__':
    app.run(debug=True)

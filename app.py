from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from datetime import datetime
import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# Load AI model
chatbot = pipeline("text-generation", model="distilgpt2")

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT, date TEXT, timestamp TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS moods
                 (id INTEGER PRIMARY KEY, mood TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Scheduler for recurring tasks
scheduler = BackgroundScheduler()
scheduler.start()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    prompt = f"User: {user_input}\nAI:"
    try:
        response = chatbot(prompt, max_length=len(prompt) + 50, num_return_sequences=1)
        ai_message = response[0]["generated_text"][len(prompt):].strip()
        return jsonify({"message": ai_message})
    except Exception as e:
        print(f"Error generating response: {e}")
        return jsonify({"error": "AI response generation failed"}), 500

@app.route("/add-task", methods=["POST"])
def add_task():
    data = request.json
    task = data.get("task", "").strip()
    date = data.get("date", "")

    if not task:
        return jsonify({"error": "Task is required"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, date, timestamp) VALUES (?, ?, ?)", (task, date, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"})

@app.route("/get-tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY timestamp DESC")
    tasks = [{"id": row[0], "task": row[1], "date": row[2], "timestamp": row[3]} for row in c.fetchall()]
    conn.close()
    return jsonify({"tasks": tasks})

@app.route("/delete-task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted successfully"})

@app.route("/set-mood", methods=["POST"])
def set_mood():
    data = request.json
    mood = data.get("mood", "").strip()

    if not mood:
        return jsonify({"error": "Mood is required"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute("INSERT INTO moods (mood, timestamp) VALUES (?, ?)", (mood, timestamp))
    conn.commit()
    conn.close()
    return jsonify({"message": "Mood updated successfully"})

@app.route("/get-mood-history", methods=["GET"])
def get_mood_history():
    conn = sqlite3.connect('ai_roommate.db')
    c = conn.cursor()
    c.execute("SELECT * FROM moods ORDER BY timestamp DESC")
    moods = [{"mood": row[1], "timestamp": row[2]} for row in c.fetchall()]
    conn.close()
    return jsonify({"mood_history": moods})

if __name__ == "__main__":
    app.run(debug=True)
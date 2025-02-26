 AI Roommate Project

Overview
The AI Roommate is a web application that combines an AI-powered chatbot, task management, and mood tracking into a single platform. It uses Flask for the backend, SQLite for data storage, and a modern frontend built with HTML, CSS (Tailwind CSS), and JavaScript.

## Features
1. AI Chatbot:
   - Interact with an AI-powered chatbot using the `distilgpt2` model from Hugging Face Transformers.
   - Real-time chat with typing indicators.

2. Task Management:
   - Add, view, and delete tasks with due dates.
   - Tasks are stored in an SQLite database.

3. Mood Tracking:
   - Track your mood (Happy, Sad, Neutral) and view mood history.
   - Visualize mood data using a bar chart powered by Chart.js.

4. Modern UI:
   - Responsive design using Tailwind CSS.
   - Easy navigation between chat, tasks, and mood sections.

Technologies Used
- Backend: Python (Flask)
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Database**: SQLite
- **AI Model**: Hugging Face Transformers (`distilgpt2`)
- **Charting**: Chart.js
- **Scheduler**: APScheduler (for recurring tasks)

Installation

Prerequisites
- Python 3.x
- Node.js (for frontend dependencies, if needed)

Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-roommate.git
   cd ai-roommate
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install Flask transformers sqlite3 apscheduler
   ```

3. Download the spaCy model (if needed):
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```
   The backend will be available at `http://localhost:5000`.

Frontend Setup
1. Open the `index.html` file in your browser.
2. Ensure the backend is running to handle API requests.

Usage
1. AI Chat:
   - Type a message in the input box and click "Send" to interact with the AI chatbot.
   - The chatbot will respond in real-time.

2. Task Management:
   - Navigate to the "Tasks" section.
   - Add a task with a description and due date.
   - View and delete tasks from the list.

3. Mood Tracking:
   - Navigate to the "Mood" section.
   - Select your mood and click "Set Mood" to log it.
   - View a bar chart of your mood history.

API Endpoints
- Chat: `POST /chat`
  - Send a message to the AI chatbot.
  - Request body: `{ "message": "Your message here" }`
  - Response: `{ "message": "AI response here" }`

- Add Task: `POST /add-task`
  - Add a new task.
  - Request body: `{ "task": "Task description", "date": "YYYY-MM-DD" }`
  - Response: `{ "message": "Task added successfully" }`

- Get Tasks: `GET /get-tasks`
  - Retrieve all tasks.
  - Response: `{ "tasks": [ { "id": 1, "task": "Task description", "date": "YYYY-MM-DD", "timestamp": "YYYY-MM-DD HH:MM:SS" } ] }`

- Delete Task: `DELETE /delete-task/<task_id>`
  - Delete a task by ID.
  - Response: `{ "message": "Task deleted successfully" }`

- Set Mood: `POST /set-mood`
  - Log a mood.
  - Request body: `{ "mood": "happy" }`
  - Response: `{ "message": "Mood updated successfully" }`

- Get Mood History: `GET /get-mood-history`
  - Retrieve mood history.
  - Response: `{ "mood_history": [ { "mood": "happy", "timestamp": "YYYY-MM-DD HH:MM:SS" } ] }`

 Screenshots
![AI Chat](screenshots/chat.png)
![Task Management](screenshots/tasks.png)
![Mood Tracking](screenshots/mood.png)

Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Contact
For questions or feedback, please contact:
- Your Name: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [sainikithavantari](https://github.com/sainikithavantari)

---

Enjoy using your AI Roommate! 🚀

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend integration

# Sample data
tasks = [
    {"id": 1, "title": "Task 1", "description": "Complete assignment", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Buy groceries", "completed": True},
]

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Get a specific task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.json
    new_task["id"] = len(tasks) + 1  # Auto-generate ID
    tasks.append(new_task)
    return jsonify(new_task), 201

# Update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task.update(request.json)
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

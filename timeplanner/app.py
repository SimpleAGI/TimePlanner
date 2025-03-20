from flask import Flask, jsonify, request
from scheduler import schedule_tasks
from analytics import visualize_time_usage
from calendar_integration import sync_with_google_calendar
from reminder import set_deadline_reminder

app = Flask(__name__)

tasks = []  # List to store tasks as dictionary items

@app.route('/')
def home():
    return "Welcome to TimePlanner!"

@app.route('/tasks', methods=['GET', 'POST', 'DELETE'])
def manage_tasks():
    global tasks
    if request.method == 'POST':
        task_data = request.json
        tasks.append({'name': task_data['name'], 'priority': task_data['priority']})
        return jsonify({'message': 'Task added', 'tasks': tasks})
    elif request.method == 'DELETE':
        task_name = request.args.get('name')
        tasks = [task for task in tasks if task['name'] != task_name]
        return jsonify({'message': f'Task \"{task_name}\" deleted', 'tasks': tasks})
    return jsonify(tasks)

@app.route('/schedule', methods=['GET'])
def schedule():
    scheduled_tasks = schedule_tasks(tasks)
    return jsonify({'scheduled_tasks': scheduled_tasks})

@app.route('/visualize', methods=['GET'])
def visualize():
    # Simulated example data
    example_data = {task['name']: 2*index + 1 for index, task in enumerate(tasks)}  # Simulate some time usage
    visualize_time_usage(example_data)
    return jsonify({'message': 'Visualization completed'})

@app.route('/sync', methods=['GET'])
def sync_calendar():
    # Perform sync
    sync_with_google_calendar()
    return jsonify({'message': 'Calendar synchronized'})

if __name__ == '__main__':
    app.run(debug=True)

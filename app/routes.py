from flask import render_template, request, redirect, url_for
from app import app


tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

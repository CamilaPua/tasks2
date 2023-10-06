from flask import Blueprint, render_template, request, redirect
from app.models.tasks_model import Task
from app import forms

# blueprint configuration
add_task_bp = Blueprint(
    'add_task_bp', __name__,
)

@add_task_bp.route('/add-task', methods=['GET', 'POST'])
def add_task():
    tasks_form = forms.Task(request.form)
    if request.method == 'POST':
        Task.add_task(tasks_form.description.data)
        return redirect('/')
    return render_template('add_task.html', tasks_form=tasks_form)

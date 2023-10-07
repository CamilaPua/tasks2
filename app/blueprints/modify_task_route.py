from flask import Blueprint, render_template, request, redirect
from app.models.tasks_model import Task
from app import forms

# blueprint configuration
modify_task_bp = Blueprint(
    'modify_task_bp', __name__,
)

@modify_task_bp.route('/modify-task', methods=['GET', 'POST'])
def modify_task():
    tasks = Task.get_tasks()
    tasks_form = forms.Task(request.form)
    if request.method == 'POST':
        if tasks_form.id:
            if tasks_form.delete.data:
                Task.del_task(tasks_form.id.data)
            else:
                Task.update_task(tasks_form.id.data)
    return render_template('modify_task.html', tasks_form=tasks_form, tasks=tasks)

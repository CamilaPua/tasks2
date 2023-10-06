from flask import Blueprint, render_template
from app.models.tasks_model import Task

# blueprint configuration
index_bp = Blueprint(
    'index_bp', __name__,
)

@index_bp.route('/')
def index():
    tasks = Task.get_tasks()
    return render_template('index.html', tasks=tasks)

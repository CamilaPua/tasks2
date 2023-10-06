from .. import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    status = db.Column(db.Boolean)

    def __init__(self, description, status=False):
        self.description = description
        self.status = status

    def __str__(self) -> str:
        return str(self.description)

    def __repr__(self):
        return self.__str__()

    def add_task(task_description):
        new_task = Task(task_description)
        db.session.add(new_task)
        db.session.commit()

    def del_task(id_task):
        task = Task.query.get(id_task)
        db.session.delete(task)
        db.session.commit()

    def update_task(id_task):
        task = Task.query.get(id_task)
        task.status = not(task.status)

    def get_tasks():
        return Task.query.all()

from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm

class Task(FlaskForm):
    id = IntegerField('ID de la tarea')
    description = StringField('Descripcion de la tarea')
    done = SubmitField('✅ Hecha')
    not_done = SubmitField('~ No hecha')
    delete = SubmitField('Eliminar')
    submit = SubmitField('Enviar')

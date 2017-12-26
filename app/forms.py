from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    pitch = StringField('Pitch',validators=[Required()])
    comment = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
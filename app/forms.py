from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TallyForm(FlaskForm):
    # [(backend, frontend)]
    q_type = SelectField('Interaction Type:', choices=
                         [("collections", "Collections"), ("research", "Research"), ("technology", "Technology"),
                          ("patron account", "Patron Account"), ("other", "Other")], validators=[DataRequired()])
    referral = BooleanField('Made Referral?')
    notes = TextAreaField('Notes')
    submit = SubmitField('Tally!')

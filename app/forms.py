from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Optional


class TallyForm(FlaskForm):
    # [(backend, frontend)]
    q_type = SelectField('Interaction Type:', choices=
                         [("Collections", "Collections"), ("Research", "Research"), ("Technology", "Technology"),
                          ("Patron Account", "Patron Account"), ("Other", "Other")], validators=[DataRequired()])
    referral = BooleanField('Made Referral?')
    notes = TextAreaField('Notes')
    submit = SubmitField('Tally!')


class ReportForm(FlaskForm):
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    start_time = TimeField("(Optional) Start Time", validators=[Optional()])
    end_time = TimeField("(Optional) End Time", validators=[Optional()])
    department = SelectField('(Optional) Department', choices=
                             [('0', 'All'), ('1', 'Information Services'), ('2', 'Youth Services')],
                             validators=[Optional()])
    q_type = SelectField('(Optional) Interaction Type:', choices=
                            [("Collections", "Collections"), ("Research", "Research"), ("Technology", "Technology"),
                            ("Patron Account", "Patron Account"), ("Other", "Other")], validators=[Optional()])
    referral = SelectField('(Optional) Referrals?', choices=
                            [('-1', "All"), ('0', "Non-Referrals"), ('1', 'Only Referrals')], validators=[Optional()])
    submit = SubmitField("Run Report")

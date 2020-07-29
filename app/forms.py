from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired
import datetime
import calendar


class TallyForm(FlaskForm):
    # [(backend, frontend)]
    q_type = SelectField('Interaction Type:', choices=
                         [("Collections", "Collections"), ("Research", "Research"), ("Technology", "Technology"),
                          ("Patron Account", "Patron Account"), ("Other", "Other")], validators=[DataRequired()])
    referral = BooleanField('Made Referral?')
    notes = TextAreaField('Notes')
    submit = SubmitField('Tally!')


class ReportForm(FlaskForm):
    # Use the calendar module to get the last day of the month to prefill the form for a one month range
    month_days = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)
    # Prefill start date with the first day of the month (conveniently, always day 1)
    start_date = DateField("Start Date", validators=[DataRequired()], default=datetime.datetime.now().replace(day=1))
    # Month days holds 2 values, the first and last day of the month IE: (1, 31), get the second value for last day
    end_date = DateField("End Date", validators=[DataRequired()], default=datetime.datetime.now().replace(day=month_days[1]))
    start_time = TimeField("Start Time", validators=[DataRequired()],
                           default=datetime.datetime.strptime("12:00 AM", "%I:%M %p"))
    end_time = TimeField("End Time", validators=[DataRequired()],
                         default=datetime.datetime.strptime("11:59 PM", "%I:%M %p"))
    department = SelectField('Department', choices=
                             [('-1', 'All'), ('1', 'Information Services'), ('2', 'Youth Services')],
                             validators=[DataRequired()], default="All")
    referral_type = SelectField('Referrals?', choices=
                            [('-1', "All"), ('0', "Non-Referrals"), ('1', 'Only Referrals')],
                            validators=[DataRequired()], default="All")
    submit = SubmitField("Run Report")


# One button form for calling export function
class ExportForm(FlaskForm):
    submit = SubmitField("Export to Excel")


from app import app
from flask import render_template, flash
from app.forms import TallyForm, ReportForm
from app import db_functions
import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info', methods=['GET', 'POST'])
def adult_info_queries():
    form = TallyForm()
    if form.validate_on_submit():
        db_functions.write_to_database(form, 1)
        flash("Tally recorded!")
    return render_template('info_services.html', title="Information Services", form=form)


@app.route('/youth', methods=['GET', 'POST'])
def youth_info_queries():
    form = TallyForm()
    if form.validate_on_submit():
        db_functions.write_to_database(form, 2)
        flash("Tally recorded!")
    return render_template('youth_services.html', title="Youth Services", form=form)


@app.route('/reports', methods=['GET', 'POST'])
def reports():
    form = ReportForm()
    if form.validate_on_submit():
        report = db_functions.read_from_database(form)
        for rp in report:
            # Convert from 24 hr time (stored in db) to 12 hr time for display
            twenty_four_hr_time = datetime.datetime.strptime(rp.time, "%H:%M")
            # strip leading zeroes from hour for presentation purposes
            rp.time = twenty_four_hr_time.strftime("%I:%M %p").lstrip("0").replace(" 0", "")
        return render_template(
            'reports.html', title="Reports", form=form, report=report, total=len(report))
    return render_template('reports.html', title="Reports", form=form)




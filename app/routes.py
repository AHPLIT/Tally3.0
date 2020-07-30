from app import app
from flask import render_template, flash
from app.forms import TallyForm, ReportForm, ExportForm
from app import db_functions
from flask_excel import make_response_from_query_sets
from app import t3exceptions
import datetime

# Global variable that will store the report database query for exporting to CSV
report = None

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info', methods=['GET', 'POST'])
def adult_info_queries():
    form = TallyForm()
    if form.validate_on_submit():
        db_functions.write_to_database(form, 1)
        flash("Tally recorded at " + datetime.datetime.now().strftime('%I:%M %p'))
    return render_template('info_services.html', title="Information Services", form=form)


@app.route('/youth', methods=['GET', 'POST'])
def youth_info_queries():
    form = TallyForm()
    if form.validate_on_submit():
        db_functions.write_to_database(form, 2)
        flash("Tally recorded at " + datetime.datetime.now().strftime('%I:%M %p'))
    return render_template('youth_services.html', title="Youth Services", form=form)


@app.route('/reports', methods=['GET', 'POST'])
def reports():
    form = ReportForm()
    export = ExportForm()
    if form.validate_on_submit():
        # Make global so we can export these results to CSV
        global report
        report = db_functions.read_from_database(form)
        for rp in report:
            # Convert from 24 hr time (stored in db) to 12 hr time for display
            twenty_four_hr_time = datetime.datetime.strptime(rp.time, "%H:%M")
            # strip leading zeroes from hour for presentation purposes
            rp.time = twenty_four_hr_time.strftime("%I:%M %p").lstrip("0").replace(" 0", "")
        return render_template(
            'reports.html', title="Reports", form=form, report=report, total=len(report), export=export)
    return render_template('reports.html', title="Reports", form=form)


@app.route('/download_csv', methods=['GET'])
def export_results():
    # Requires initialization of Excel library done in __init__.py to work properly
    # Report is a global variable that holds the last run report query from the reports page
    if report is None:
        t3exceptions.Error("Attempted to export CSV before report query was run. Did the button display too early?")
    else:
        for r in report:
            if r.department == "1":
                r.department = "Information"
            elif r.department == "2":
                r.department = "Youth"
            else:
                t3exceptions.Error("Unable to parse department, was a new one added?")

            if r.referral == 0:
                r.referral = "No"
            elif r.referral == 1:
                r.referral = "Yes"
            else:
                t3exceptions.Error("Unable to convert referrals to strings when exporting CSV")

        today = datetime.datetime.now().strftime("%Y.%m.%d")
        f_name = today + "_Tally3-Report"
        output = make_response_from_query_sets(report, ['date', 'time', 'department', 'q_type', 'referral', 'notes'],
                                               "csv", file_name=f_name)
        return output



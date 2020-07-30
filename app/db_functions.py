import datetime
from flask_excel import make_response_from_query_sets
from app import t3exceptions
from app.models import *


def write_to_database(form, department_number):
    date_string = datetime.datetime.now().strftime('%Y-%m-%d')
    time_string = datetime.datetime.now().strftime('%H:%M')
    # WTForms returns a boolean, SQLite needs an integer. Do a quick conversion
    if form.referral.data:
        ref_int = 1  # True
    else:
        ref_int = 0  # False
    response = Queries(
        q_type=form.q_type.data,
        department=department_number,
        date=date_string,
        time=time_string,
        notes=form.notes.data,
        referral=ref_int)
    db.session.add(response)
    db.session.commit()


def read_from_database(form):
    start_date = form.start_date.data
    end_date = form.end_date.data
    start_time = form.start_time.data
    end_time = form.end_time.data
    q_type = form.q_type_report.data
    department = form.department.data
    referrals = form.referral_type.data

    # Probably a better way to modularize this, but
    if q_type == "All":
        # -1 == All
        if department == "-1" and referrals == "-1":
            # This & syntax is specific to SQLAlchemy for properly querying the db
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time)).all()
        elif department == "-1" and referrals != "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (referrals == Queries.referral)).all()
        elif department != "-1" and referrals == "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (department == Queries.department)).all()
        elif department != "-1" and referrals != "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (department == Queries.department) & (referrals == Queries.referral)).all()
        else:
            # Custom exception. This should never happen so if it does, fail loudly.
            raise t3exceptions.Error("If statement failure! Incorrect combination of department and referral refs")
    else:
        if department == "-1" and referrals == "-1":
            # This & syntax is specific to SQLAlchemy for properly querying the db
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (q_type == Queries.q_type)).all()
        elif department == "-1" and referrals != "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (referrals == Queries.referral) & (q_type == Queries.q_type)).all()
        elif department != "-1" and referrals == "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (department == Queries.department) & (q_type == Queries.q_type)).all()
        elif department != "-1" and referrals != "-1":
            report = db.session.query(Queries).filter(
                (start_date <= Queries.date) & (end_date >= Queries.date) & (start_time <= Queries.time) &
                (end_time >= Queries.time) & (department == Queries.department) & (referrals == Queries.referral)
                & (q_type == Queries.q_type)).all()
        else:
            # Custom exception. This should never happen so if it does, fail loudly.
            raise t3exceptions.Error("If statement failure! Incorrect combination of department and referral refs")
    return report


def export_to_excel(form):
    response = read_from_database(form)
    return make_response_from_query_sets(response, ['Department', 'Date', 'Time', 'Notes', 'Referral'], 'csv')

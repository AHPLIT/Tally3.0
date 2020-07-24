import datetime
from app import t3exceptions
from app.models import *


def write_to_database(form, department_number):
    date_string = datetime.datetime.now().strftime('%Y-%m-%d')
    time_string = datetime.datetime.now().strftime('%H:%M')
    if form.referral.data:
        ref_int = 1
    else:
        ref_int = 0
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
    department = form.department.data
    referrals = form.referral.data
    # -1 == All
    if department == "-1" and referrals == "-1":
        report = db.session.query(Queries).filter(
            (start_date <= Queries.date) & (end_date >= Queries.date) &(start_time <= Queries.time) &
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
        raise t3exceptions.Error("If statement failure! Incorrect combination of department and referral refs")
    return report




import datetime
from app.models import *


def write_to_database(form, department_number):
    date_string = datetime.datetime.now().strftime('%Y-%m-%d')
    time_string = datetime.datetime.now().strftime('%I:%M %p')
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
    referrals = form.referrals.data
    report = db.session.query(Queries).filter((start_date <= Queries.date) & (end_date >= Queries.date)).all()
    return report

from app import db


class QueryTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_type = db.Column(db.Text, unique=True, nullable=False)


class Queries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_type = db.Column(db.Integer, db.ForeignKey(QueryTypes.id))
    department = db.Column(db.Text, nullable=False)
    time = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    # SQLite doesn't have bool data types so referral is an int
    referral = db.Column(db.Integer, nullable=False)
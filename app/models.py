from app import db

class Journals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sourceid = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False, unique=True)
    total_docs_2017 = db.Column(db.String(64))
    total_docs_3_years = db.Column(db.String(64))
    total_refs = db.Column(db.String(64))
    total_cites_3_years = db.Column(db.String(64))
    citable_docs_3_years = db.Column(db.String(64))
    cites_per_doc_2_years = db.Column(db.String(64))
    refs_per_doc = db.Column(db.String(64))
    country = db.Column(db.String(64))
    publisher = db.Column(db.String(64), nullable=False)
    rating = db.Column(db.String(64))


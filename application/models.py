# -*- coding: utf-8 -*-
from datetime import datetime
from application import db


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text, pub_date=None):
        self.title = title
        self.text = text
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Entry %s>' % self.title

# -*- coding:utf-8 -*-
from extensions import db
from datetime import datetime


class DatasourceModel(db.Model):
    __table_args__ = {"schema": "test"}
    __tablename__ = 'datasource'

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_del = db.Column(db.Boolean, default=False)
    type = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String, default='')
    host = db.Column(db.String)
    port = db.Column(db.Integer, default=-1)
    db_name = db.Column(db.String)
    db_user = db.Column(db.String)
    db_psw = db.Column(db.String)
    operator = db.Column(db.String, default='')
    owner = db.Column(db.String, default='')

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        def format(value):
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d %H:%M:%S")
            return value

        return {i.name: format(getattr(self, i.name)) for i in self.__table__.columns}

# -*- coding:utf-8 -*-
from extensions import db
from datetime import datetime


class ScheduleModel(db.Model):
    __table_args__ = {"schema": "test"}
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_del = db.Column(db.Boolean, default=False)
    schedule_name = db.Column(db.String)
    schedule_interval = db.Column(db.String)
    operator = db.Column(db.String)

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

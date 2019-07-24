# -*- coding:utf-8 -*-
from extensions import db
from datetime import datetime
from sqlalchemy.sql import func


class JobModel(db.Model):
    __table_args__ = {"schema": "test"}
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_del = db.Column(db.Boolean, default=False)
    schedule_id = db.Column(db.Integer)
    job_num = db.Column(db.Integer)
    job_name = db.Column(db.String)
    layer = db.Column(db.String)
    source_id = db.Column(db.Integer)
    source_table_id = db.Column(db.Integer, default=-1)
    sql_text = db.Column(db.Text, default='')
    target_id = db.Column(db.String, default='')
    target_table = db.Column(db.String, default='')
    description = db.Column(db.String, default='')
    dependent_jobs = db.Column(db.String, default='')
    operator = db.Column(db.String, default='')
    is_valid = db.Column(db.Boolean, default=True)
    version = db.Column(db.Integer, default=1)
    job_type = db.Column(db.String, default='SPARK')
    job_submit_args = db.Column(db.String, default='')
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

    def new_to_save(self, values):

        dict = {i.name: getattr(self, i.name) for i in self.__table__.columns}
        dict.update(values)
        del dict["id"]
        del dict["create_time"]
        del dict["update_time"]
        dict["version"] = dict["version"] + 1

        obj = JobModel(**dict)
        db.session.add(obj)
        db.session.commit()
        return obj

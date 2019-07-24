# -*-coding:utf-8-*-
from flask_restful import Resource, reqparse
from models.job import JobModel
from flask import jsonify
import json


class Job(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, id):
        obj = JobModel.get_by_id(id)

        if obj:
            s = obj.to_dict()
            return {"data": s, "msg": ""}

        return {"msg": "Item not found!", "data": ""}, 404

    def put(self, id):
        obj = JobModel.get_by_id(id)

        if obj:
            self.parser.add_argument("data", type=str, required=True)
            args = self.parser.parse_args()
            data = json.loads(args["data"])
            try:
                if data.get("sql_text") and not obj.sql_text == data.get("sql_text"):
                    obj.update({"is_valid": False})
                    obj = obj.new_to_save(data)
                else:
                    obj.update(data)
            except Exception as e:
                print(e)
                return {"msg": "Update error!", "data": ""}, 404
            return {"data": obj.to_dict(), "msg": ""}
        return {"msg": "Item not found!", "data": ""}, 404

    def delete(self, id):
        obj = JobModel.get_by_id(id)

        if obj:
            try:
                obj.delete()
            except Exception as e:
                print(e)
                return {"msg": "Delete error!", "data": ""}, 404
            return {"data": obj.to_dict(), "msg": ""}
        return {"msg": "Item not found!", "data": ""}, 404


class JobList(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument("limit", type=str)
        self.parser.add_argument("offset", type=str)
        args = self.parser.parse_args()
        limit = args["limit"]
        offset = args["offset"]
        query = JobModel.query

        result = query.limit(limit).offset(offset)
        total = query.count()
        return jsonify({"data": [i.to_dict() for i in result.all()], "msg": "", "total": total})

    def post(self):
        self.parser.add_argument("data", type=str, required=True)
        args = self.parser.parse_args()
        data = json.loads(args["data"])

        obj = JobModel(**data)
        try:
            obj.save()
        except Exception as e:
            print(e)
            return {"msg": "Insert error!", "data": ""}, 404

        return {"data": obj.to_dict(), "msg": ""}

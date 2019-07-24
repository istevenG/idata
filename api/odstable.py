# -*-coding:utf-8-*-
from flask_restful import Resource, reqparse
from models.odstable import OdsTableModel
from flask import jsonify
import json


class OdsTable(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, id):
        obj = OdsTableModel.get_by_id(id)

        if obj:
            s = obj.to_dict()
            return {"data": s, "msg": ""}

        return {"msg": "Item not found!", "data": ""}, 404

    def put(self, id):
        obj = OdsTableModel.get_by_id(id)

        if obj:
            self.add_argument("data", type=str, required=True)
            args = self.parser.parse_args()
            data = json.loads(args["data"])
            try:
                obj.update(data)
            except Exception as e:
                print(e)
                return {"msg": "Update error!", "data": ""}, 404
            return {"data": obj.to_dict(), "msg": ""}
        return {"msg": "Item not found!", "data": ""}, 404

    def delete(self, id):
        obj = OdsTableModel.get_by_id(id)

        if obj:
            try:
                obj.delete()
            except Exception as e:
                print(e)
                return {"msg": "Delete error!", "data": ""}, 404
            return {"data": obj.to_dict(), "msg": ""}
        return {"msg": "Item not found!", "data": ""}, 404


class OdsTableList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument("limit", type=str)
        self.parser.add_argument("offset", type=str)
        args = self.parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        query = OdsTableModel.query
        result = query.limit(limit).offset(offset)
        total = query.count()
        return jsonify({"data": [i.to_dict() for i in result.all()], "msg": "", "total": total})

    def post(self):
        self.parser.add_argument("data", type=str, required=True)
        args = self.parser.parse_args()
        data = json.loads(args["data"])

        obj = OdsTableModel(**data)
        try:
            obj.save()
        except Exception as e:
            print(e)
            return {"msg": "Insert error!", "data": ""}, 404

        return {"data": obj.to_dict(), "msg": ""}

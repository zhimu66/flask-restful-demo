# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource
from flask_restful_swagger import swagger

from app.api.base import Service
from app.utils.core import db
from app.utils.response import ResMsg
from app.models.model import Article

swagger_test = Blueprint('swagger_test', __name__, url_prefix='/api/swagger_test')
api = swagger.docs(Api(swagger_test), description='swagger_test', api_spec_url="/show")


class AddArticle(Resource):
    @swagger.operation(
        description="swagger_test 新增文章",
        summary='swagger_test 新增文章',
        parameters=[{
            "name": "title",
            "description": "文章标题",
            "required": True,
            "paramType": "form",
            "dataType": 'string'
        }, {
            "name": "body1", # 不能为body
            "description": "文章内容",
            "required": True,
            "paramType": "form",
            "dataType": 'string'
        }, {
            "name": "author_id",
            "description": "作者id",
            "required": True,
            "paramType": "form",
            "dataType": 'int'
        }])
    def post(self):
        body = dict(request.form)
        body['body'] = body.pop("body1", "")

        article = Article(**body)
        db.session.add(article)
        db.session.commit()

        res = ResMsg()
        res.update(data=True)
        return res.data

api.add_resource(AddArticle, 'addarticle')

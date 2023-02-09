from flask import Flask, request, redirect
from flask_restful import Resource, Api

from src.entities.url import Url

from src.repositories import InMemoryRepository

from src.use_cases.create_url import CreateUrlUseCase, CreateUrlRequest
from src.use_cases.get_url import GetUrlUseCase, GetUrlRequest


app = Flask(__name__)
api = Api(app)

url_repository = InMemoryRepository()


class CreateUrlRouter(Resource):
    def post(self):
        create_url_use_case = CreateUrlUseCase(url_repository)
        data_request = CreateUrlRequest(**request.get_json(force=True))
        
        new_url = create_url_use_case.execute(data_request)
        
        return new_url.object._props.__dict__


class RedirectUrl(Resource):
    def get(self, hash):
        get_url_use_case = GetUrlUseCase(url_repository)
        data_request = GetUrlRequest(hash=hash)
        
        get_url = get_url_use_case.execute(**data_request)
        
        if not get_url:
            return {'error': 'not found!'}
        
        return redirect(get_url.object.redirect_url)


api.add_resource(CreateUrlRouter, '/create_url')
api.add_resource(RedirectUrl, '/<string:hash>')

if __name__ == '__main__':
    app.run(debug=True)
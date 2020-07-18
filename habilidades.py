from flask_restful import Resource


habilidades = ['Python','Java','C','C#']

class ListaHabilidades(Resource):
    def get(self):
        return habilidades
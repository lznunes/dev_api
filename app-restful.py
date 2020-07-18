from flask import Flask, request
from flask_restful import  Resource, Api
import  json
from habilidades import ListaHabilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{'id':0, 'nome' : 'Luiz', 'habilidades':['Python', 'Java']},
                  { 'id':1,'nome':'Antonio', 'habilidades':['Javascript', 'C#']}]


class Desenvolvedore(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe" .format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            response = {'status':'error', 'mensagem':'Erro desconhecido procure o Adm'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro {} excluido' .format(id)}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao: int = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedore, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(ListaHabilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)
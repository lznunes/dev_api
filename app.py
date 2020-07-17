from flask import Flask, jsonify, request
import  json

app = Flask(__name__)

desenvolvedores = [{'id':0, 'nome' : 'Luiz', 'habilidades':['Python', 'Java']},
                  { 'id':1,'nome':'Antonio', 'habilidades':['Javascript', 'C#']}]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = "Desenvolvedor de ID {} não existe" .format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            response = {'status':'error', 'mensagem':'Erro desconhecido procure o Adm'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluido'})

@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao: int = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run()


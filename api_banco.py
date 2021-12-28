from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import sqlalchemy
import json

desenvolvedores = []
acrescentar=[]

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/cadastro')

df = pd.read_sql_table('bancos',engine)
print(df.shape[0])
b =(df.loc[0:0])

app = Flask(__name__)
api = Api(app)

i=0
while (i<=(df.shape[0]-1)):
    b = (df.loc[i:i])
    codigo = int(b["codigo_de_compensacao"].head())
    banco = str(b["Nome_da_Instituicao"].head())
    acrescentar = [
        {
            'codigo': codigo,
            'banco': banco,
        },
    ]
    desenvolvedores.append(acrescentar)
    i = i + 1

#devolve um banco pelo codigo
class Desenvolvedor(Resource):
    def get(self,codigo):
        id = json.loads(request.data)
        try:
            i=0
            while (i <= (df.shape[0] - 1)):
                c = (df.loc[i:i])
                if (id == int(c["codigo_de_compensacao"].head())):
                    d=i
                i=i+1
            response = desenvolvedores[d]
        except IndexError:
            mensagem = 'Codigo do Banco não existe'.format(codigo)
            response = {'status': 'erro ', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro ', 'mensagem': mensagem}
        return response

# Lista todos os bancos
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

api.add_resource(Desenvolvedor, '/bancos/<string:codigo>/')
api.add_resource(ListaDesenvolvedores, '/bancos/')

if __name__ == '__main__':
    app.run(debug=True)
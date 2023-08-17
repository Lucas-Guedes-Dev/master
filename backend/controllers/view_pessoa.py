from flask.views import MethodView  
from flask import request
from flask import jsonify
from db.connection import Connection
from db.models import Pessoa

class ViewPessoa(MethodView):
    def __init__(self):
        super().__init__()
        self.session = Connection().create_session()

    def post(self):
        if request.method == 'POST':
            dados_list = request.get_json()
            
            if self.salva_pessoa(dados_list):
                return jsonify({"sucesso": "Cadastro da pessoa realizado ou alterado com sucesso!"})
            
            return jsonify({'error': "Verifique o cadastro e tente novamente"})
        
    def salva_pessoa(self, dados_list):

        for dados_dict in dados_list:
            
            pessoa_dict = self.session.query(Pessoa).filter(dados_dict['cpf'] == Pessoa.cpf).first()

            if pessoa_dict:
                pessoa_dict.empresa=dados_dict['empresa']
                pessoa_dict.nome=dados_dict['nome']
                pessoa_dict.email=dados_dict['email']
                pessoa_dict.cpf =dados_dict['cpf']
                pessoa_dict.telefone=dados_dict['telefone']
                pessoa_dict.rua=dados_dict['rua']
                pessoa_dict.bairro =dados_dict['bairro']
                pessoa_dict.cidade =dados_dict['cidade']
                pessoa_dict.estado =dados_dict['estado']
                pessoa_dict.numero =dados_dict['numero']
            else:
                new_pessoa = Pessoa(**dados_dict)
                print(new_pessoa)
                self.session.add(new_pessoa)
                self.session.commit()

        return True
        

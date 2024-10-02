import pymongo
from bson import ObjectId
from datetime import datetime
import os

class PersonDatabase:
    def __init__(self):
        # Conectar ao MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["controle_pessoas"]
        self.collection = self.db["pessoas"]

    def salvar_pessoa(self, dados):
        """Salva uma nova pessoa ou atualiza uma existente"""
        if '_id' in dados:
            # Atualizar pessoa existente
            pessoa_id = dados['_id']
            del dados['_id']
            dados['data_atualizacao'] = datetime.now()
            self.collection.update_one({'_id': ObjectId(pessoa_id)}, {'$set': dados})
            return str(pessoa_id)
        else:
            # Inserir nova pessoa
            dados['data_cadastro'] = datetime.now()
            dados['data_atualizacao'] = datetime.now()
            resultado = self.collection.insert_one(dados)
            return str(resultado.inserted_id)

    def consultar_pessoa(self, pessoa_id):
        """Consulta uma pessoa pelo ID"""
        return self.collection.find_one({'_id': ObjectId(pessoa_id)})

    def listar_pessoas(self):
        """Lista todas as pessoas"""
        return list(self.collection.find())

    def excluir_pessoa(self, pessoa_id):
        """Exclui uma pessoa pelo ID"""
        resultado = self.collection.delete_one({'_id': ObjectId(pessoa_id)})
        return resultado.deleted_count > 0

    def fechar_conexao(self):
        """Fecha a conexão com o MongoDB"""
        self.client.close()

    def atualizar_imagem_pessoa(self, pessoa_id, imagem_path):
        """Atualiza o caminho da imagem de uma pessoa"""
        self.collection.update_one(
            {'_id': ObjectId(pessoa_id)},
            {'$set': {'imagem_path': imagem_path}}
        )

# Funções auxiliares para conversão de dados

def converter_para_documento(dados):
    """Converte os dados do formulário para um documento MongoDB"""
    try:
        documento = {
            'nome': dados['nome'],
            'idade': int(dados['idade']) if dados['idade'] else None,
            'altura': float(dados['altura']) if dados['altura'] else None,
            'peso': float(dados['peso']) if dados['peso'] else None,
            'cidade': dados['cidade'],
            'data_nascimento': datetime.strptime(dados['data_nascimento'], '%d/%m/%Y') if dados['data_nascimento'] else None,
            'descricao': dados['descricao']
        }
        if 'imagem_path' in dados and dados['imagem_path']:
            documento['imagem_path'] = dados['imagem_path']
        return documento
    except ValueError as e:
        raise ValueError(f"Erro ao converter dados: {str(e)}")

def converter_para_formulario(documento):
    """Converte um documento MongoDB para o formato do formulário"""
    formulario = {
        '_id': str(documento['_id']),
        'nome': documento['nome'],
        'idade': str(documento['idade']) if documento['idade'] is not None else '',
        'altura': str(documento['altura']) if documento['altura'] is not None else '',
        'peso': str(documento['peso']) if documento['peso'] is not None else '',
        'cidade': documento['cidade'],
        'data_nascimento': documento['data_nascimento'].strftime('%d/%m/%Y') if documento['data_nascimento'] else '',
        'data_cadastro': documento['data_cadastro'].strftime('%d/%m/%Y'),
        'data_atualizacao': documento['data_atualizacao'].strftime('%d/%m/%Y'),
        'descricao': documento['descricao']
    }
    if 'imagem_path' in documento:
        formulario['imagem_path'] = documento['imagem_path']
    return formulario

class GerenciadorPessoas:
    def __init__(self):
        self.db = PersonDatabase()

    def inserir_pessoa(self, dados):
        return self.db.salvar_pessoa(dados)

    def consultar_pessoa(self, pessoa_id):
        return self.db.consultar_pessoa(pessoa_id)

    def atualizar_pessoa(self, pessoa_id, dados):
        pessoa = self.db.consultar_pessoa(pessoa_id)
        if pessoa:
            dados['_id'] = pessoa['_id']
            self.db.salvar_pessoa(dados)
            return True
        return False

    def excluir_pessoa(self, pessoa_id):
        return self.db.excluir_pessoa(pessoa_id)

    def listar_pessoas(self):
        """Lista todas as pessoas no formato adequado para a interface"""
        pessoas = self.db.listar_pessoas()
        return [converter_para_formulario(pessoa) for pessoa in pessoas]

    def fechar_conexao(self):
        self.db.fechar_conexao()

    def atualizar_imagem_pessoa(self, pessoa_id, imagem_path):
        self.db.atualizar_imagem_pessoa(pessoa_id, imagem_path)

    def buscar_pessoas_por_nome(self, nome):
        """Busca pessoas cujo nome contém o termo de busca"""
        try:
            regex = {'$regex': nome, '$options': 'i'}
            pessoas = self.db.collection.find({'nome': regex})
            return [converter_para_formulario(pessoa) for pessoa in pessoas]
        except Exception as e:
            raise Exception(f"Erro ao buscar pessoas por nome: {str(e)}")

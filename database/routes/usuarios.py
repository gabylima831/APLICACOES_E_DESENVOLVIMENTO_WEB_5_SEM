from flask import Blueprint, request, jsonify
from database.models import db, Usuario

usuarios_bp = Blueprint("usuarios", __name__)

# Inserir usuário (POST)
@usuarios_bp.route("/inserir", methods=["POST"])
def inserir():
    dados = request.get_json()
    if not dados or "nome" not in dados or "curso" not in dados:
        return jsonify({"erro": "Campos 'nome' e 'curso' são obrigatórios"}), 400

    novo_usuario = Usuario(nome=dados["nome"], curso=dados["curso"])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário inserido com sucesso!", "usuario": novo_usuario.to_dict()}), 201

# Listar usuários (GET)
@usuarios_bp.route("/usuarios", methods=["GET"])
def listar():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios]), 200

# Atualizar usuário (PUT)
@usuarios_bp.route("/atualizar/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    usuario = Usuario.query.get_or_404(id)

    if "nome" in dados:
        usuario.nome = dados["nome"]
    if "curso" in dados:
        usuario.curso = dados["curso"]

    db.session.commit()
    return jsonify({"mensagem": "Usuário atualizado com sucesso!", "usuario": usuario.to_dict()}), 200

# Deletar usuário (DELETE)
@usuarios_bp.route("/deletar/<int:id>", methods=["DELETE"])
def deletar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário removido com sucesso!"}), 200
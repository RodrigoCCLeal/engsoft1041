from flask_openapi3 import Tag

from api.controllers.produto_schemas import ProdutoBuscaSchema, ProdutoSchema
from api.presenters.error_presenter import ErrorSchema, apresenta_erro
from api.presenters.produto_presenter import (
    ListagemProdutosSchema,
    ProdutoDelSchema,
    ProdutoViewSchema,
    apresenta_produto,
    apresenta_produtos,
    apresenta_remocao,
)
from core.usecases.erros import ProdutoJaExiste, ProdutoNaoEncontrado


def registrar_rotas_produto(app, adicionar, listar, buscar, remover) -> None:
    produto_tag = Tag(name="Produto", description="Operações com produtos")

    @app.post(
        "/produto",
        tags=[produto_tag],
        responses={200: ProdutoViewSchema, 409: ErrorSchema},
    )
    def post_produto(body: ProdutoSchema):
        try:
            produto = adicionar.executar(
                body.nome,
                body.quantidade,
                body.valor,
            )
        except ProdutoJaExiste as erro:
            return apresenta_erro(str(erro)).model_dump(), 409
        return apresenta_produto(produto).model_dump(), 200

    @app.get(
        "/produtos",
        tags=[produto_tag],
        responses={200: ListagemProdutosSchema},
    )
    def get_produtos():
        produtos = listar.executar()
        return apresenta_produtos(produtos).model_dump(), 200

    @app.get(
        "/produto",
        tags=[produto_tag],
        responses={200: ProdutoViewSchema, 404: ErrorSchema},
    )
    def get_produto(query: ProdutoBuscaSchema):
        try:
            produto = buscar.executar(query.nome)
        except ProdutoNaoEncontrado as erro:
            return apresenta_erro(str(erro)).model_dump(), 404
        return apresenta_produto(produto).model_dump(), 200

    @app.delete(
        "/produto",
        tags=[produto_tag],
        responses={200: ProdutoDelSchema, 404: ErrorSchema},
    )
    def delete_produto(query: ProdutoBuscaSchema):
        try:
            remover.executar(query.nome)
        except ProdutoNaoEncontrado as erro:
            return apresenta_erro(str(erro)).model_dump(), 404
        return apresenta_remocao(query.nome).model_dump(), 200

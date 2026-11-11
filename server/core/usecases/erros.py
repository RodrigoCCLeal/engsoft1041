class ProdutoJaExiste(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Produto '{nome}' já existe na base")


class ProdutoNaoEncontrado(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Produto '{nome}' não encontrado na base")

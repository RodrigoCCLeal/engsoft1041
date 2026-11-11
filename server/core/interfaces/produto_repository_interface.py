from abc import ABC, abstractmethod
from typing import Optional

from core.entities.produto import Produto


class ProdutoRepositoryInterface(ABC):
    @abstractmethod
    def salvar(self, produto: Produto) -> Produto:
        ...

    @abstractmethod
    def listar(self) -> list[Produto]:
        ...

    @abstractmethod
    def buscar_por_nome(self, nome: str) -> Optional[Produto]:
        ...

    @abstractmethod
    def remover_por_nome(self, nome: str) -> bool:
        ...

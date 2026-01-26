from abc import ABC, abstractmethod

class ProdutoInterface(ABC):
    
    @abstractmethod
    def criar_produto(self, nome:str) -> None: pass
    
    @abstractmethod
    def produto_all(self) -> None: pass
    
    @abstractmethod
    def produto_status(self, id_produto:int) -> None: pass
    
    @abstractmethod
    def produto_delete(self, id_produto:int) -> None: pass
    
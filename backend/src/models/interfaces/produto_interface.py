from abc import ABC, abstractmethod

class ProdutoInterface(ABC):
    
    @abstractmethod
    def criar_produto() -> None: pass
    
    @abstractmethod
    def produto_all() -> None: pass
    
    @abstractmethod
    def produto_status() -> None: pass
    
    @abstractmethod
    def produto_delete() -> None: pass
    
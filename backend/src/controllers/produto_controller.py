from src.models.interfaces.produto_interface import ProdutoInterface

class ProdutoController:
    
    def __init__(self, produto_repository: ProdutoInterface):
        self.produto_repo = produto_repository
        
    def criar_produto(self, nome:str):
        return self.produto_repo.criar_produto(nome)
    
    def listar_todos_produtos(self):
        return self.produto_repo.produto_all()
    
    def mudar_status_produto(self, id_produto:int):
        return self.produto_repo.produto_status(id_produto)
    
    def deletar_produto(self, id_produto: int):
        return self.produto_repo.produto_delete(id_produto)
    
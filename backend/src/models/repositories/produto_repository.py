from ..interfaces.produto_interface import ProdutoInterface
from ..produto_model import Produto
from src.settings.extersions import db

class ProdutoRepository(ProdutoInterface):
    
    def __init__(self):
        pass
    
    def criar_produto(self, nome: str) -> Produto:        
        novo_produto = Produto(nome=nome, status=False)
        db.session.add(novo_produto)
        db.session.commit()
        return novo_produto
        
    def produto_all(self) -> list[tuple]:    
        lista_produtos = db.session.query(Produto).all()
        return lista_produtos
    
    def produto_status(self, id_produto: int) -> None:
        produto_select = db.session.query(Produto).filter(Produto.id == id_produto).first()
        if produto_select:
            produto_select.id=1
            db.session.commit()
            return produto_select
        return None    
    
    def produto_delete(self, id_produto: int) -> None:
        produto_select = db.session.query(Produto).filter(Produto.id == id_produto).first()
        if produto_select:
            db.session.delete(produto_select)
            db.session.commit()
            return produto_select
        return None
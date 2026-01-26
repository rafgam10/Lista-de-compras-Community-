from abc import ABC, abstractmethod

class UserInterface(ABC):
    
    @abstractmethod
    def criar_user() -> None: pass
    
    @abstractmethod
    def user_all() -> None: pass
    
    @abstractmethod
    def user_edit() -> None: pass
    
    @abstractmethod
    def user_delete() -> None: pass
    
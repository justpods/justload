from abc import ABC, abstractmethod

class BaseLoader(ABC):

    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def load(self): ...

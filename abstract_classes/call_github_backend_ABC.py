from abc import ABC, abstractmethod

class call_github_backend_ABC(ABC):
    @abstractmethod
    async def call_github_repo():
        pass
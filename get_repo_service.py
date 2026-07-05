import requests
from services.call_github_backend import call_github_backend

class get_repo_service_method:
    def __init__(self):
     self.call = call_github_backend()

    def get_repos(self):
        return self.call.call_github_repo()
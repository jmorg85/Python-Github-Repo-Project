import asyncio
import aiohttp
from services.call_github_backend import call_github_backend

class get_repo_service_method:
    def __init__(self, repo_url = "https://api.github.com/users/jmorg85/repos"):
     self.call = call_github_backend()
     self.repo_url = repo_url

    async def get_repos(self):
        async with aiohttp.ClientSession() as session:
            return await self.call.call_github_repo(session, self.repo_url)
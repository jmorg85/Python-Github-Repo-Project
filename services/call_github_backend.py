from abstract_classes.call_github_backend_ABC import call_github_backend_ABC
import aiohttp
import asyncio


class call_github_backend(call_github_backend_ABC):
    async def call_github_repo(self, session, url):
        async with session.get(url) as response:
            return await response.json()
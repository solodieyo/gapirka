import logging
from typing import Optional, Any, override

from aiohttp import ClientSession
from dataclass_rest.http.aiohttp import AiohttpClient as BaseAiohttpClient
from dataclass_rest.http_request import HttpRequest

logger = logging.getLogger(__name__)
logger.level = logging.ERROR


class AiohttpClient(BaseAiohttpClient):

	def __init__(
		self,
		base_url: str,
		session: Optional[ClientSession] = None,
		query_params: Optional[dict] = None,
	):
		super().__init__(
			base_url=base_url,
			session=session
		)
		self.query_params = query_params

	@override
	async def do_request(self, request: HttpRequest) -> Any:
		if self.query_params:
			request.query_params.update(self.query_params)
		response = await super().do_request(request)
		logger.info("Request %s", request)
		logger.info("Response %s", await response.text())
		return response

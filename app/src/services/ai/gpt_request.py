from freeGPT import AsyncClient


async def gtp_request(prompt: str) -> str:
	response = await AsyncClient.create_completion(
		model="gpt3",
		prompt=prompt
	)
	return response

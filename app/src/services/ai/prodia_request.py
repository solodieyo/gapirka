from io import BytesIO

from freeGPT import AsyncClient
from PIL import Image


async def prodia_request(prompt: str) -> None:
	response = await AsyncClient.create_generation(
		model="pollinations",
		prompt=prompt
	)
	Image.open(BytesIO(response)).save("image.jpeg")


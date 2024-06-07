import logging


def setup_logging():
	logging.basicConfig(
		level=logging.INFO,
		format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
	)
	logger = logging.getLogger(__name__)
	logger.info("Starting bot")
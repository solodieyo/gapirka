import os
import tomllib
from pathlib import Path
from typing import TypeVar

from adaptix import Retort

T = TypeVar("T")
DEFAULT_CONFIG_PATH = r"C:\Users\SOLO\2to3\gapirka\app\config.toml"


def read_toml(path: Path) -> dict:
	with Path.open(path, "rb") as f:
		return tomllib.load(f)


def load_config(
	config_type: type[T],
	config_scope: str | None = None,
	path: Path | None = None,
) -> T:
	if path is None:
		path = Path(os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH))

	data = read_toml(path)

	if config_scope is not None:
		data = data[config_scope]

	dcf = Retort()
	return dcf.load(data, config_type)
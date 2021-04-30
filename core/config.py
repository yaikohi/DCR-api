from starlette.config import Config
from starlette.datastructures import Secret


APP_NAME = "pioDash-DCR"
APP_VERSION = "0.0.2"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH")

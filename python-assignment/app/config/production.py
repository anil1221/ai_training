from app.config.base import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG: bool = False
    API_RATE_LIMIT: int = 1000
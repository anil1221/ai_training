from app.config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    RATE_LIMITING: int = 400
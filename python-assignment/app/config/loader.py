import os

from app.config.development import DevelopmentConfig
from app.config.production import ProductionConfig


environment = os.getenv("ENVIRONMENT", "development")


def get_settings():
    if environment == "production":
        return ProductionConfig()

    return DevelopmentConfig()


settings = get_settings()
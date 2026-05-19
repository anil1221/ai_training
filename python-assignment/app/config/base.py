from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class BaseConfig(BaseSettings):
  APP_NAME: str = "MyApp"
  ENVIRONMENT: str = "development"


  DB_HOST: str
  DB_PORT: str
  DB_USER: str
  DB_PASSWORD: str

  EMAIL_ENABLED: bool = False
  RATE_LIMITING: int = 50

  model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
  )
  
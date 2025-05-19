from pydantic import BaseSettings

class Settings(BaseSettings):
    route_prefix: str = "/predict"
    model_name: str = "distilbert-base-uncased"

    class Config:
        env_file = ".env"

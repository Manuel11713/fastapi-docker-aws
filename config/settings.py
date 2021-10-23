from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    items_per_user: int = 50
    database_user: str = os.getenv('DATABASE_USER')
    database_password: str = os.getenv('DATABASE_PASSWORD')
    database_host: str = os.getenv('DATABASE_HOST')
    database_name: str = os.getenv('DATABASE_NAME')
    stripe_public_key: str = os.getenv('STRIPE_PUBLIC_KEY')

    class Config:
        env_file = '.env'


settings = Settings()

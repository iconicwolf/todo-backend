from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database settings
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "tododb"
    DB_HOST: str = "db"
    DB_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # App settings
    APP_NAME: str = "Todo List API"
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

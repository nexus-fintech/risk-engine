from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """
    Centralized application configuration.
    Reads environment variables or uses default values.
    """
    PROJECT_NAME: str = "Nexus Risk Engine"
    API_V1_STR: str = "/api/v1"
    
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:8080", "http://localhost:4200"]

    MIN_SCORE_APPROVE: int = 650
    BASE_INTEREST_RATE: float = 0.15  # 15%

    model_config = {
        "case_sensitive": True,
        "env_file": ".env"
    }

settings = Settings()

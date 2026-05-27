"""
AXIOS OS Configuration Settings

Centralized configuration management.
"""

from pydantic import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings(BaseSettings):
    """
    Global AXIOS OS settings.
    """

    # --------------------------------------------------
    # System Identity
    # --------------------------------------------------

    SYSTEM_NAME: str = "AXIOS OS"
    VERSION: str = "0.1.0"

    # --------------------------------------------------
    # Server Configuration
    # --------------------------------------------------

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # --------------------------------------------------
    # API Keys
    # --------------------------------------------------

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    HUGGINGFACE_API_KEY: str = ""

    # --------------------------------------------------
    # Model Configuration
    # --------------------------------------------------

    MODEL_NAME: str = "deepseek-ai/deepseek-coder"
    MODEL_PATH: str = "./models"

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_LEVEL: str = "INFO"
    LOG_PATH: str = "./logs"

    # --------------------------------------------------
    # Memory Systems
    # --------------------------------------------------

    MEMORY_PATH: str = "./data/memory"
    EMBEDDINGS_PATH: str = "./data/embeddings"

    # --------------------------------------------------
    # Telemetry
    # --------------------------------------------------

    ENABLE_TELEMETRY: bool = True

    # --------------------------------------------------
    # Constraint Systems
    # --------------------------------------------------

    ENABLE_CONSTRAINTS: bool = True
    ENABLE_DECEPTION_MONITOR: bool = True

    # --------------------------------------------------
    # Identity Engine
    # --------------------------------------------------

    ENABLE_IDENTITY_TRACKING: bool = True

    # --------------------------------------------------
    # Meta Governance
    # --------------------------------------------------

    ENABLE_META_REFLECTION: bool = True

    # --------------------------------------------------
    # Simulation Mode
    # --------------------------------------------------

    ENABLE_SIMULATIONS: bool = False

    # --------------------------------------------------
    # Pydantic Config
    # --------------------------------------------------

    class Config:
        env_file = ".env"
        case_sensitive = True

# config/settings.py

import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

# 🔑 API Keys
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "no-key-found")

# 📁 Data Path
CSV_FILE_PATH: str = os.getenv("CSV_FILE_PATH", str(BASE_DIR / "data/NY-House-Dataset.csv"))

# 🛠️ Other Configs (optional)
DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# config.py
import os
from typing import Final

# Optional: load .env in development when python-dotenv is installed
# (keeps behavior unchanged if python-dotenv is not installed)
if os.getenv("ZODIAC_LOAD_DOTENV", "1") == "1":
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
    except Exception:
        # python-dotenv is optional; continue if not installed
        pass

API_URL: Final[str] = os.getenv(
    "ZODIAC_API_URL",
    "https://divineapi.com/api/1.0/get_daily_horoscope.php"
)

API_KEY: Final[str] = os.getenv("ZODIAC_API_KEY", "")

# simple headers dict is sufficient
HEADERS: Final[dict] = {
    "Content-Type": os.getenv("ZODIAC_CONTENT_TYPE", "application/x-www-form-urlencoded")
}

# Defaults and types
DEFAULT_SIGN: Final[str] = os.getenv("ZODIAC_DEFAULT_SIGN", "gemini")
try:
    API_TIMEOUT: Final[int] = int(os.getenv("ZODIAC_TIMEOUT_SECONDS", "10"))
except ValueError:
    API_TIMEOUT = 10

# Secret key for Flask sessions (should be set in production)
SECRET_KEY: Final[str] = os.getenv("SECRET_KEY", os.getenv("FLASK_SECRET_KEY", ""))

# Quick runtime check helper (optional)
def check_config():
    return {
        "API_URL": API_URL,
        "API_KEY_SET": bool(API_KEY),
        "HEADERS": HEADERS,
        "DEFAULT_SIGN": DEFAULT_SIGN,
        "API_TIMEOUT": API_TIMEOUT,
        "SECRET_KEY_SET": bool(SECRET_KEY),
    }
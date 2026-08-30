# quantbot/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """全專案共用的設定。來源是 .env，程式碼裡不出現任何密鑰。"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    okx_api_key: str = ""
    okx_api_secret: str = ""
    okx_testnet: bool = True

    postgres_dsn: str = "postgresql://qiantbot:belliwu56@localhost:5432/market"

    default_symbol: str = "BTCUSDT"
    default_market: str = "spot"


settings = Settings()

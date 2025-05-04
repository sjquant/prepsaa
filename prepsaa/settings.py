from pathlib import Path
from pydantic import SecretStr
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
)

CONFIG_DIR = Path.home() / ".config" / "prepsaa"
CONFIG_FILE = CONFIG_DIR / "config.json"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="PREPSAA_", json_file=CONFIG_FILE, extra="ignore"
    )

    default_model: str = "gpt-4.1"
    alternative_model: str = "o3-mini"
    notion_database_id: str = ""
    notion_api_key: SecretStr = SecretStr("")
    anthropic_api_key: SecretStr = SecretStr("")
    openai_api_key: SecretStr = SecretStr("")
    google_api_key: SecretStr = SecretStr("")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            JsonConfigSettingsSource(settings_cls),
        )


settings = Settings()

__all__ = ["settings"]

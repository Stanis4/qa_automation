from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")


class BrowserConfig(BaseConfig):
    type: str
    base_url: str

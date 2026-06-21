from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    azure_ai_foundry_endpoint: str = ""
    azure_ai_foundry_api_key: str = ""
    azure_sql_connection: str = ""
    azure_ad_tenant_id: str = ""
    azure_ad_client_id: str = ""
    azure_ad_client_secret: str = ""

    model_config = {
        "env_file": ".env",
    }


settings = Settings()

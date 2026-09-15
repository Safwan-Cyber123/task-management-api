from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    DB_Connection: str
    secret_key:str
    algo:str
    exp_time:int
    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    MAIL_FROM :str
    MAIL_SERVER :str
    MAIL_FROM_NAME:str

settings = Settings()

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "czr_default_secret"
    DEBUG = True

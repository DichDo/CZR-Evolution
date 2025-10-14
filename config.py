import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'czr_secret_key')
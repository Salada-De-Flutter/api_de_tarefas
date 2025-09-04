import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "wcc@2023")
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres.baealdslrwvkejjjgtqr:Tapohameno_717@aws-0-us-east-2.pooler.supabase.com:6543/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
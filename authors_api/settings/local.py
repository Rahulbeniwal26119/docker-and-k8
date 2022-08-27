from email.policy import default
from .base import * 
from .base import env 

DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY", 
                 default='django-insecure-6a#*qeb2#!mq0_gz!xex$nftsobb1w3=x6&4izs(#wqua321by')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

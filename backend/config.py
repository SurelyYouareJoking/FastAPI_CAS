# define your config here
# coding=gbk
import os

from starlette.datastructures import Secret

DEBUG = os.getenv("DEBUG", True)

DATABASE_URL = os.getenv("DATABASE_URL", None)
MAX_CONNECTIONS_COUNT = 10
MIN_CONNECTIONS_COUNT = 4

ALLOWED_HOSTS = [
    "*",
]

SECRET_KEY = Secret(os.getenv("SECRET_KEY", "application-secret"))

# db connect config
DB = {
    "user": 'root',
    "pass": 'Xjswj@by2020j',
    "host": '120.253.41.92',
    "port": '8201',
    "db": 'tt',
}


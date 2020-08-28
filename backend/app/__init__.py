from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.staticfiles import StaticFiles

from app.core.controller import router
from app.utils.db_loader import connect_db, disconnect_db
from app.utils.error_handlers import http_error_handler, http_422_error_handler
from app.utils.middleware import AuthMiddleware
import config

app = FastAPI()


# handling static files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=500,  # 浏览器缓存CORS返回结果的最大时长，默认为600(单位秒)
)

app.add_middleware(SessionMiddleware, secret_key='ST-3KugLz80ptYAnrr0kiVj8MWzwwWVczwI4Fvd7V3qgGtpDsVkvA21LdadhixSW')

app.add_middleware(AuthMiddleware)

# connect to database
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", disconnect_db)

# error handling
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

# include various routes
app.include_router(router, prefix="/core", tags=["core"])

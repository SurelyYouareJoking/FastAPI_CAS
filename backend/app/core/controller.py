import logging
import datetime
import jwt

from cas import CASClient
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.requests import Request

from app.models.user import DBUser
from app.utils.cas import get_cas
from app.utils.database import get_db
from config import SECRET_KEY

router = APIRouter()


@router.get("/login", tags=["auth"])
async def login_route(
        request: Request,
        ticket: str = None,
        cas_client: CASClient = Depends(get_cas),
        db: Session = Depends(get_db)
):
    current_time = datetime.datetime.now()
    if not ticket:
        # No ticket, the request come from end user, send to CAS login
        cas_login_url = cas_client.get_login_url()
        return RedirectResponse(url=cas_login_url)

    username, attributes, _ = cas_client.verify_ticket(ticket)
    request.session['username'] = username

    if not username:
        return {
            "success": 0,
            "message": "Invalid user! Retry logging in!"
        }
    else:
        logging.debug(f"CAS verify ticket response: user: {username}")

        existing = await DBUser.get_by_username(db, username)
        if existing:
            db_user = {"last_login": current_time}
            await DBUser.update(db, username, db_user)
        else:
            # add the initial state as unanswered
            db_user = DBUser(username=username,
                             last_login=current_time,
                             first_login=current_time,
                             )
            await DBUser.add(db, db_user)

        access_token = jwt.encode({'username': username}, str(SECRET_KEY), algorithm="HS256").decode()
        return {"access_token": access_token,
                "username": username,
                "token_type": "bearer",
                }


@router.get("/")
async def read_root(request: Request):
    return {"Hello": request.session.get("username")}


@router.get("/register")
async def register(username: str, db: Session = Depends(get_db)):
    db_user = await DBUser.get_by_username(db, username)
    if db_user:
        return db_user

    db_user = DBUser(username=username)
    await DBUser.add(db, db_user)

    return db_user

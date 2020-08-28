from starlette.responses import RedirectResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.cas import cas_client


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # request.session['github_user'] = 123
        return await call_next(request)

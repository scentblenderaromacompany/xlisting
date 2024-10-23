from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

class CSPMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, policy: str):
        super().__init__(app)
        self.policy = policy

    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["Content-Security-Policy"] = self.policy
        return response

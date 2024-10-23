from fastapi import FastAPI
from backend.middleware.csp_middleware import CSPMiddleware
from backend.middleware.rate_limit_middleware import limiter, add_rate_limit
from backend.routes.routes import router as routes_router
from backend.routes.auth_routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define your CSP policy
csp_policy = \"""
default-src 'self';
script-src 'self' 'unsafe-inline' https://trusted.cdn.com;
style-src 'self' 'unsafe-inline' https://trusted.cdn.com;
img-src 'self' data:;
connect-src 'self' https://api.trusted.com;
font-src 'self' https://fonts.gstatic.com;
frame-src 'none';
object-src 'none';
base-uri 'self';
form-action 'self';
\"\"\"

# Add CSP Middleware
app.add_middleware(CSPMiddleware, policy=csp_policy)

# Add Rate Limiting Middleware
add_rate_limit(app)

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourfrontenddomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(routes_router)
app.include_router(auth_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

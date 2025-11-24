from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.endpoints import risk

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Credit risk evaluation microservice with Hybrid AI.",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Allows Java Backend (Spring Boot) and Frontend (Angular) to consume this service.
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Prefix: /api/v1/evaluate-risk
app.include_router(risk.router, prefix=settings.API_V1_STR, tags=["Risk Engine"])

@app.get("/health", tags=["Health Check"])
def health_check():
    """Simple endpoint to verify that the service is alive."""
    return {"status": "ok", "service": settings.PROJECT_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

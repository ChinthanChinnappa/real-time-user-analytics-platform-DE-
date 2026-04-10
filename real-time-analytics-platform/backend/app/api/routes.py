from fastapi import APIRouter
from .analytics import router as analytics_router

router = APIRouter()

# Include analytics routes
router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
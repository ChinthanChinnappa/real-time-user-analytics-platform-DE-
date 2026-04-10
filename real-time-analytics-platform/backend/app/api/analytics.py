from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..services.analytics_service import AnalyticsService
from ..schemas.schemas import AnalyticsResponse

router = APIRouter()

@router.get("/summary", response_model=AnalyticsResponse)
async def get_analytics_summary(db: Session = Depends(get_db)):
    """Get analytics summary."""
    service = AnalyticsService(db)
    return service.get_summary()

@router.get("/events/{event_type}")
async def get_events_by_type(event_type: str, db: Session = Depends(get_db)):
    """Get events by type."""
    service = AnalyticsService(db)
    return service.get_events_by_type(event_type)

@router.get("/users/{user_id}")
async def get_user_events(user_id: str, db: Session = Depends(get_db)):
    """Get events for a specific user."""
    service = AnalyticsService(db)
    return service.get_user_events(user_id)
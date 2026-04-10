from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.models import UserEvent
from ..schemas.schemas import AnalyticsResponse

class AnalyticsService:
    def __init__(self, db: Session):
        self.db = db

    def get_summary(self) -> AnalyticsResponse:
        """Get analytics summary."""
        # Total events
        total_events = self.db.query(func.count(UserEvent.id)).scalar()

        # Unique users
        unique_users = self.db.query(func.count(func.distinct(UserEvent.user_id))).scalar()

        # Top pages
        top_pages_query = self.db.query(
            UserEvent.page,
            func.count(UserEvent.id).label('count')
        ).group_by(UserEvent.page).order_by(func.count(UserEvent.id).desc()).limit(5)

        top_pages = {row.page: row.count for row in top_pages_query}

        # Event types
        event_types_query = self.db.query(
            UserEvent.event_type,
            func.count(UserEvent.id).label('count')
        ).group_by(UserEvent.event_type)

        event_types = {row.event_type: row.count for row in event_types_query}

        return AnalyticsResponse(
            total_events=total_events,
            unique_users=unique_users,
            top_pages=top_pages,
            event_types=event_types
        )

    def get_events_by_type(self, event_type: str):
        """Get events by type."""
        return self.db.query(UserEvent).filter(UserEvent.event_type == event_type).all()

    def get_user_events(self, user_id: str):
        """Get events for a specific user."""
        return self.db.query(UserEvent).filter(UserEvent.user_id == user_id).all()
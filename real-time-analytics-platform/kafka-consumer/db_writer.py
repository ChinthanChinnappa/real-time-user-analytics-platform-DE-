from sqlalchemy.orm import sessionmaker
from models import UserEvent, engine
from datetime import datetime

class DBWriter:
    def __init__(self):
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def write_event(self, event_data):
        """Write event to database."""
        db = self.SessionLocal()
        try:
            # Convert timestamp string to datetime
            timestamp = datetime.fromisoformat(event_data['timestamp'])

            user_event = UserEvent(
                event_type=event_data['event_type'],
                user_id=event_data['user_id'],
                page=event_data['page'],
                timestamp=timestamp,
                value=event_data.get('value')
            )

            db.add(user_event)
            db.commit()
            print(f"Written event to DB: {user_event.id}")
        except Exception as e:
            db.rollback()
            print(f"Error writing to DB: {e}")
        finally:
            db.close()

    def close(self):
        """Close the database connection."""
        pass
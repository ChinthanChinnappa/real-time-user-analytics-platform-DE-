import pandas as pd
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/analytics')

def aggregate_data():
    """Aggregate analytics data for reporting."""
    engine = create_engine(DATABASE_URL)

    # Daily aggregations
    with engine.connect() as conn:
        # Create aggregated table if not exists
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS daily_aggregates (
                date DATE PRIMARY KEY,
                total_events INTEGER,
                unique_users INTEGER,
                top_page TEXT
            )
        """))

        # Insert daily aggregates
        conn.execute(text("""
            INSERT INTO daily_aggregates (date, total_events, unique_users, top_page)
            SELECT
                DATE(timestamp) as date,
                COUNT(*) as total_events,
                COUNT(DISTINCT user_id) as unique_users,
                (SELECT page FROM user_events
                 WHERE DATE(timestamp) = DATE(ue.timestamp)
                 GROUP BY page ORDER BY COUNT(*) DESC LIMIT 1) as top_page
            FROM user_events ue
            WHERE DATE(timestamp) = CURRENT_DATE - INTERVAL '1 day'
            GROUP BY DATE(timestamp)
            ON CONFLICT (date) DO UPDATE SET
                total_events = EXCLUDED.total_events,
                unique_users = EXCLUDED.unique_users,
                top_page = EXCLUDED.top_page
        """))

        conn.commit()

    print("Aggregated data for yesterday")

    engine.dispose()
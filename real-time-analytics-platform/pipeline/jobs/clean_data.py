import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/analytics')

def clean_data():
    """Clean and preprocess analytics data."""
    engine = create_engine(DATABASE_URL)

    # Read data from database
    query = "SELECT * FROM user_events WHERE timestamp >= CURRENT_DATE - INTERVAL '1 day'"
    df = pd.read_sql(query, engine)

    # Basic cleaning
    df = df.dropna(subset=['event_type', 'user_id'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Write back cleaned data (in a real scenario, you'd write to a staging table)
    print(f"Cleaned {len(df)} records")
    print(df.head())

    engine.dispose()
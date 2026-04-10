-- Initialize PostgreSQL database
CREATE DATABASE analytics;
\c analytics;

-- Create user_events table
CREATE TABLE user_events (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    page VARCHAR(100),
    timestamp TIMESTAMP NOT NULL,
    value FLOAT
);

-- Create indexes
CREATE INDEX idx_event_type ON user_events(event_type);
CREATE INDEX idx_user_id ON user_events(user_id);
CREATE INDEX idx_timestamp ON user_events(timestamp);

-- Create daily_aggregates table for batch processing
CREATE TABLE daily_aggregates (
    date DATE PRIMARY KEY,
    total_events INTEGER,
    unique_users INTEGER,
    top_page TEXT
);
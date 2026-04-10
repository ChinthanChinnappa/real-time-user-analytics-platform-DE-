import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC_NAME = 'user_events'
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/analytics')
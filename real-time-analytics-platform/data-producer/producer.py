import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer
from config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME

def generate_event():
    """Generate a random user event."""
    events = ['page_view', 'click', 'purchase', 'login', 'logout']
    users = [f'user_{i}' for i in range(1, 101)]
    pages = ['home', 'products', 'cart', 'checkout', 'profile']

    return {
        'event_type': random.choice(events),
        'user_id': random.choice(users),
        'page': random.choice(pages),
        'timestamp': datetime.now().isoformat(),
        'value': random.randint(1, 1000) if random.random() > 0.5 else None
    }

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print(f"Starting data producer. Sending events to topic: {TOPIC_NAME}")

    try:
        while True:
            event = generate_event()
            producer.send(TOPIC_NAME, event)
            print(f"Sent event: {event}")
            time.sleep(random.uniform(0.1, 1.0))  # Random delay between 0.1-1 second
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.close()

if __name__ == "__main__":
    main()
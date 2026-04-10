import json
from kafka import KafkaConsumer
from db_writer import DBWriter
from config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='analytics_consumer',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    db_writer = DBWriter()

    logger.info(f"Starting Kafka consumer for topic: {TOPIC_NAME}")

    try:
        for message in consumer:
            event = message.value
            logger.info(f"Received event: {event}")
            db_writer.write_event(event)
    except KeyboardInterrupt:
        logger.info("Stopping consumer...")
    finally:
        consumer.close()
        db_writer.close()

if __name__ == "__main__":
    main()
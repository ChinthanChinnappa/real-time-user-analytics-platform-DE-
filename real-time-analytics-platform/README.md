# Real-Time Analytics Platform

A comprehensive real-time analytics platform built with Kafka, FastAPI, Airflow, and React.

## Architecture

- **Data Producer**: Simulates user events and sends them to Kafka
- **Kafka Consumer**: Consumes messages from Kafka and writes to PostgreSQL
- **Backend**: FastAPI service providing REST APIs for analytics
- **Pipeline**: Airflow DAGs for batch processing and data aggregation
- **Dashboard**: React frontend for visualizing analytics data
- **Infra**: Docker configurations for Kafka, PostgreSQL, and Airflow

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and configure environment variables
3. Run `docker-compose up` to start all services
4. Access the dashboard at `http://localhost:3000`

## Development

- Backend API: `http://localhost:8000`
- Airflow UI: `http://localhost:8080`
- Kafka: `localhost:9092`
- PostgreSQL: `localhost:5432`
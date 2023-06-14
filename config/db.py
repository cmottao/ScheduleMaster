from sqlalchemy import create_engine

# Creates a connection to the PostgreSQL database named "schedule_master" using the psycopg2 driver.
engine = create_engine(
    f'postgresql+psycopg2://postgres:password@localhost:5432/schedule_master'
)
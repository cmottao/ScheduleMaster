from sqlalchemy import create_engine

engine = create_engine(
    f'postgresql+psycopg2://postgres:password@localhost:5432/schedule_master'
)
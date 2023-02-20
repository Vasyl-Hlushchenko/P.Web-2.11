from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://rest_app:567234@localhost:5432/rest_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





    # docker run -d \
	# --name some-postgres \
	# -p 5432:5432 \
	# -e POSTGRES_PASSWORD=567234 \
	# -e POSTGRES_USER=rest_app \
	# -d \
	# postgres
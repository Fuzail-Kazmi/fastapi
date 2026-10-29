from app.core.database import Base, engine
from app.db.models.users import User
from app.db.models.products import Product


def create_tables():
    Base.metadata.create_all(bind=engine)

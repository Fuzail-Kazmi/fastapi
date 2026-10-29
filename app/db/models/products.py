from typing import Optional
from sqlalchemy import String, Column, Integer
from app.core.database import Base


class Product(Base):
    __tablename__ = "Products"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    product_price = Column(Integer, index=True)
    product_stock = Column(Integer, index=True)



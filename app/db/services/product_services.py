from app.db.models.products import Product
from sqlalchemy.orm import Session
from app.db.schemas.product_schema import CreateProduct


def get_products(db: Session):
    return db.query(Product).all()


def create_product(db: Session, data: CreateProduct):
    product_instance = Product(**data.model_dump())
    db.add(product_instance)
    db.commit()
    db.refresh(product_instance)
    return product_instance


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()


def update_product(db: Session, product: CreateProduct, product_id: int):
    product_queryset = (
        db.query(Product).filter(Product.product_id == product_id).first()
    )
    if product_id:
        for key, value in product.model_dump().items():
            setattr(product_queryset, key, value)
            db.commit()
            db.refresh(product_queryset)
        return product_queryset

def delete_product(db: Session, product_id: int):
    product_queryset = (db.query(Product).filter(Product.product_id == product_id).first())
    if product_id:
            db.delete(product_queryset)
            db.commit()
    return product_queryset

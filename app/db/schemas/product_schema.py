from pydantic import BaseModel


class ProductBase(BaseModel):
    product_name : str
    product_price : int
    product_stock : int


class CreateProduct(ProductBase):
    pass


class Product(ProductBase):
    product_id : int

    class config:
        from_attribute = True

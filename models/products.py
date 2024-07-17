from sqlalchemy import Column, String, Integer, Boolean, Float
from .base import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, nullable=False)
    product_name = Column(String, index=True, nullable=False)
    product_category = Column(String, index=True, nullable=False)
    is_equipment = Column(Boolean)
    kmfl_classification = Column(String)
    is_rmnch = Column(Boolean)
    is_in_647_tracer_list = Column(Boolean)
    avg_price_kes = Column(Float)

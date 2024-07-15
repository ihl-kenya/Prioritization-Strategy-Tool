from sqlalchemy import Column, String, Integer, ForeignKey, Float
from .base import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    key = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    ven = Column(String, nullable=False)
    pack_size = Column(String)
    price_kes = Column(Float)
    quantity_required_for_one_year = Column(Float)
    facility_id = Column(String, ForeignKey("facilities.facility_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))

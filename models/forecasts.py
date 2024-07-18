from sqlalchemy import Column, String, Integer, Float, ForeignKey
from .base import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    forecast_id = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(String, ForeignKey("facilities.org_id"))
    quantity_required_for_one_year = Column(Float)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    ven = Column(String, index=True)
    price_kes = Column(Float)
    value_of_quantities_required_for_12_months = Column(Float)
    funding = Column(String, index=True)
    pack_size = Column(String)
    financial_year = Column(String)

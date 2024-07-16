from sqlalchemy import Column, String, Integer, Boolean, Float
from .base import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    key = Column(Integer, primary_key=True, autoincrement=True)
    county = Column(String, nullable=False, index=True)
    sub_county = Column(String, nullable=False, index=True)
    facility_name = Column(String, nullable=False, index=True)
    keph_level = Column(String, nullable=False, index=True)
    product_category = Column(String, nullable=False, index=True)
    ven = Column(String, index=True)
    funding = Column(String, index=True)
    product_name = Column(String, nullable=False)
    pack_size = Column(String)
    price_kes = Column(Float)
    quantity_required_for_one_year = Column(Float)
    value_of_quantities_required_for_12_months = Column(Float)
    is_equipment = Column(Boolean, index=True)
    kmfl_classification = Column(String, index=True)
    is_rmnch = Column(Boolean, index=True)
    is_in_647_tracer_list = Column(Boolean, index=True)
    product_id = Column(String, nullable=False, index=True)

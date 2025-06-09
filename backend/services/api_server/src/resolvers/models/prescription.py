from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    raw_text = Column(Text, nullable=False)
    parsed_drugs = Column(String(512), nullable=True)  # comma-separated
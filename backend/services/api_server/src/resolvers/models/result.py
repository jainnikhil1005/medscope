from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InteractionResult(Base):
    __tablename__ = "interaction_results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    prescription1_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False)
    prescription2_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False)

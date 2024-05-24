from sqlalchemy import Column, BigInteger, Double
from db.base import Base

class User(Base):
    __tablename__ = 'user'
    
    user_id = Column(BigInteger, primary_key=True, 
                     unique=True, autoincrement=False)
    lat = Column(Double, nullable=True)
    long = Column(Double, nullable=True)

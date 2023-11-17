from sqlalchemy import Column, String, Integer
from shared.base import Base 

class Transformed(Base):
    __tablename__ = "transformed"

    id = Column(Integer, primary_key=True, autoincrement=True)
    airplane = Column(Integer, foreign_key=True)
    record_time = Column(String)
    phase_of_flight = Column(Integer)
    phase_of_flight_navigation = Column(Integer)
    message1 = Column(Integer)
    message2 = Column(Integer)

    def __repr__(self):
        return f"<Transformed(airplane={self.airplane}, record_time={self.record_time}, phase_of_flight={self.phase_of_flight}, phase_of_flight_navigation={self.phase_of_flight_navigation}, message1={self.message1}, message2={self.message2})>"
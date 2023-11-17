from sqlalchemy import Column, String, Integer, Boolen, DateTime
from shared.base import Base 

class Predicted(Base):
    __tablename__ = "predicted"

    id = Column(Integer, primary_key=True, autoincrement=True)
    airplane_id = Column(Integer, foreign_key='transformed.airplane')
    bleed_fail1_50 = Column(Boolen)
    bleed_fail2_50 = Column(Boolen)
    bleed_fail1_100 = Column(Boolen)
    bleed_fail2_100 = Column(Boolen)
    time = Column(DateTime)
    bleed_fail1 = Column(Boolen)
    bleed_fail2 = Column(Boolen)

    def __repr__(self):
        return f"<Predicted(airplane={self.airplane}, record_time={self.record_time}, phase_of_flight={self.phase_of_flight}, phase_of_flight_navigation={self.phase_of_flight_navigation}, message1={self.message1}, message2={self.message2})>"
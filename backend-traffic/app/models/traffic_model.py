from pydantic import BaseModel

class TrafficData(BaseModel):
    frc: str
    currentSpeed: float
    freeFlowSpeed: float
    currentTravelTime: float
    freeFlowTravelTime: float
    confidence: float
    roadClosure: bool

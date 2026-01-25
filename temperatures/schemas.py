from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TemperatureBase(BaseModel):
    date_time: datetime
    temperature: str


class TemperatureCreate(TemperatureBase):
    city_id: int


class Temperature(TemperatureBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    city_id: int

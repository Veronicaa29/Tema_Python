from typing import List

from pydantic import BaseModel, Field

class FactorialInput(BaseModel):
    number: int = Field(..., ge=0)

class FibonacciInput(BaseModel):
    number: int = Field(..., ge=0)

class PowerInput(BaseModel):
    base: float
    exp: float

class RequestRecord(BaseModel):
    id: int
    operation: str
    input: str
    result: str
    timestamp: str

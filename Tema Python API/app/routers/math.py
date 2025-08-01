from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.models import (
    FactorialInput,
    FibonacciInput,
    PowerInput,
    RequestRecord,
)
from app.services import math_service, logging_service
import sqlite3

router = APIRouter(prefix="/math", tags=["Math Operations"])


@router.post("/factorial")
def calc_factorial(data: FactorialInput):
    result = math_service.factorial(data.number)
    logging_service.log_operation("factorial", data.dict(), str(result))
    return {"result": result}


@router.post("/fibonacci")
def calc_fibonacci(data: FibonacciInput):
    result = math_service.fibonacci(data.number)
    logging_service.log_operation("fibonacci", data.dict(), str(result))
    return {"result": result}


@router.post("/power")
def calc_power(data: PowerInput):
    result = math_service.power(data.base, data.exp)
    logging_service.log_operation("power", data.dict(), str(result))
    return {"result": result}


@router.get("/history", response_model=List[RequestRecord])
def get_history():
    try:
        conn = sqlite3.connect("operations.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM requests ORDER BY id DESC LIMIT 20")
        rows = cursor.fetchall()
        conn.close()

        return [
            RequestRecord(
                id=row[0],
                operation=row[1],
                input=row[2],
                result=row[3],
                timestamp=row[4]
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

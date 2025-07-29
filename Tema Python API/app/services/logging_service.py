import json
from app.db.database import save_request

def log_operation(operation: str, input_data: dict, result: str):
    json_input = json.dumps(input_data)
    save_request(operation, json_input, result)

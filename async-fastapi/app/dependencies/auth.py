from fastapi import Header
from fastapi import HTTPException


API_KEY = "secret-api-key"


async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return x_api_key
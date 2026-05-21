from fastapi import Depends
from fastapi import FastAPI

from app.middleware.timing import (add_process_time_header)

from app.dependencies.auth import (verify_api_key)

from app.dependencies.rate_limiter import (rate_limiter)

from app.services.async_data_service import (fetch_data)

app = FastAPI()

app.middleware("http")(add_process_time_header)


@app.get("/data")
async def get_data(api_key: str = Depends(verify_api_key)):

    await rate_limiter(api_key)

    result = await fetch_data()

    return result
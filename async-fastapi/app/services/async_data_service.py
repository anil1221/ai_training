import asyncio


async def fetch_data():

    print("Fetching data from async service...")

    await asyncio.sleep(2)

    return {
        "message": "Async data retrieved successfully",
        "status": "success"
    }
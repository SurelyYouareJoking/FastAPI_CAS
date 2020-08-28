from app.utils.database import database


async def connect_db():
    await database.connect()


async def disconnect_db():
    await database.disconnect()

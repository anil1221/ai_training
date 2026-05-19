from app.config.loader import settings


def connect_database():
    print("Connecting to database...")
    print(f"Host: {settings.DB_HOST}")
    print(f"Port: {settings.DB_PORT}")
    print(f"User: {settings.DB_USER}")
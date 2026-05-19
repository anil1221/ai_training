from app.config.loader import settings
from app.services.database_service import connect_database
from app.services.email_service import start_email_service


def main():
    print("Application Starting...")
    print(f"App Name: {settings.APP_NAME}")
    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"Rate Limit: {settings.RATE_LIMITING}")

    connect_database()
    start_email_service()

if __name__ == "__main__":
    main()  
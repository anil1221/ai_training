from app.config.loader import settings


def start_email_service():
    if settings.EMAIL_ENABLED:
        print("Email service started")
    else:
        print("Email service disabled")
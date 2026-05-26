import re

def mask_pii(text):

    # Mask emails
    text = re.sub(r'\S+@\S+', '[EMAIL_MASKED]', text)

    # Mask phone numbers
    text = re.sub(r'\d{10}', '[PHONE_MASKED]', text)

    return text
def summarize_context(text):
    words = text.split()
    if len(words) > 50:
        return (" ".join(words[:50])+ " ...")

    return text
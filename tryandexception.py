import logging

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Error dividing %s by %s: %s", a, b, e)
        return None
    return result
divide(-8,0)
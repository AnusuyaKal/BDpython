import logging

# Configure logging
logging.basicConfig(filename='exampl2.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        # Log the exception
        logging.exception("Error occurred while dividing by zero")
    except Exception as e:
        # Log any other exceptions
        logging.exception("An error occurred: %s", str(e))
    else:
        return result

# Example usage
result = divide(10, 0)

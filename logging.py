import logging
# Configure the logger
logging.basicConfig(filename="app.log", level=logging.INFO)
# Perform an operation with error handling
def perform_operation():
    try:
        # Code to perform the operation
        logging.info("Operation executed successfully")
    except Exception as e:
        logging.error("An error occurred during the operation: %s", str(e))
# Usage example
perform_operation()

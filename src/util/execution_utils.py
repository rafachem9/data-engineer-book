import time
from util.variables import logger


def execution(func, process_name):
    # Mark the start time
    start_time = time.time()
    logger.info(f"Starting {process_name}")

    # Execute the function
    func()

    # Mark the end time
    end_time = time.time()

    # Calculate and display the duration
    duration = end_time - start_time
    logger.info(f"Execution time: {round(duration, 1)} seconds")

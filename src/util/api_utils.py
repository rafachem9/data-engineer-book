import requests


def get_data_api(logger, url_name, url, params=None, headers=None):
    """
    Fetches data from a specified API endpoint.

    :param logger: Logger object for logging messages.
    :param url_name: A human-readable name for the URL for logging purposes.
    :param url: URL of the API endpoint.
    :param params: Dictionary of parameters to be sent in the query string.
    :return: The JSON response from the API if the request was successful, None otherwise.
    """
    logger.info(f'Data extraction process started from {url_name}')
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()  # Parse JSON response
        else:
            logger.error(f'Connection error with code: {response.status_code}')
            return None
    except Exception as e:
        logger.error(f'Error fetching data from {url_name}: {str(e)}')
        return None


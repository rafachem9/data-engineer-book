from projectutils.api_utils import get_data_api


def extract_data_seeclickfix(logger, url_name, url, params):
    """
    Extracts data from SeeClickFix API, handling pagination to collect all available data.

    :param logger: Logger object for logging messages.
    :param url_name: A human-readable name for the URL for logging purposes.
    :param url: URL of the API endpoint.
    :param params: Dictionary of parameters to be sent in the query string.
    :return: List of all issues extracted from the API across all pages.
    """
    # Get data from the first page
    response = get_data_api(logger, url_name, url, params)
    if not response:
        logger.error('Failed to retrieve data from the first page.')
        return []

    data = response.get('issues', [])
    pagination = response.get('metadata', {}).get('pagination', {})
    total_pages = pagination.get('pages', 1)
    logger.info(f'Starting to process the received data, total pages: {total_pages}')

    # Iterate through all pages to collect data
    for page in range(2, total_pages + 1):  # Start from page 2 because we already have page 1
        params['page'] = page  # Update params dict to request the next page
        logger.info(f'Extracting data from page {page}')
        response = get_data_api(logger, url_name, url, params)
        if response:
            data += response.get('issues', [])
        else:
            logger.error(f'Failed to retrieve data from page {page}')

    logger.info(f'Data successfully received, total issues: {len(data)}')
    return data

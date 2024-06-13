from elasticsearch import Elasticsearch
from elasticsearch import helpers


def connect_elastic(logger, elastic_host, elastic_user, elastic_pass):
    """
    Connect to an Elasticsearch instance.

    :param logger: Logger object for logging messages.
    :param elastic_host: URL of the Elasticsearch host.
    :param elastic_user: Username for Elasticsearch authentication.
    :param elastic_pass: Password for Elasticsearch authentication.
    :return: Elasticsearch client instance or None if connection fails.
    """
    logger.info('Connecting to Elasticsearch')
    try:
        es_client = Elasticsearch(
            [elastic_host],
            http_auth=(elastic_user, elastic_pass),
            verify_certs=False  # Consider setting up proper SSL/TLS and enabling certificate verification
        )
        logger.info('Successfully connected to Elasticsearch')
        return es_client
    except Exception as e:
        logger.error(f"Failed to connect to Elasticsearch: {str(e)}")
        return None


def insert_data_elasticsearch(logger, elastic_host, elastic_user, elastic_pass, index_name, data):
    """
    Insert data into an Elasticsearch index.

    :param logger: Logger object for logging messages.
    :param elastic_host: URL of the Elasticsearch host.
    :param elastic_user: Username for Elasticsearch authentication.
    :param elastic_pass: Password for Elasticsearch authentication.
    :param index_name: Name of the Elasticsearch index where data will be inserted.
    :param data: List of dictionaries representing the documents to insert.
    """
    es_client = connect_elastic(logger, elastic_host, elastic_user, elastic_pass)
    if es_client is not None:
        try:
            logger.info(f"Starting data insertion into index '{index_name}'. Total documents: {len(data)}")
            actions = [{"_index": index_name, "_source": doc} for doc in data]
            success, _ = helpers.bulk(es_client, actions)
            logger.info(f"Successfully inserted {success} documents into index '{index_name}'.")
        except Exception as e:
            logger.error(f"Error inserting data into index '{index_name}': {str(e)}")
    else:
        logger.error("Elasticsearch client is not available. Data insertion skipped.")

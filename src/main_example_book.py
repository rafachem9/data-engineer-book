import os

from util.variables import logger
from projectutils.elastic_utils import insert_data_elasticsearch

from etl.extract_data import extract_data_seeclickfix

# API information
logger.info('Data extraction process started from seeclickfix')
params = {'place_url': 'bernalillo-county', 'per_page': '100'}
url = 'https://seeclickfix.com/api/v2/issues?'
url_name = 'seeclickfix'

# ElasticSearch
elastic_user = os.getenv('elastic_user')
elastic_pass = os.getenv('elastic_pass')
elastic_host = os.getenv('elastic_host')


all_data = extract_data_seeclickfix(logger, url_name, url, params)
actions = []

index_name = "scf_v3"
for review in all_data:
    close_timestamp = review['closed_at']
    if close_timestamp:
        close_date = review['closed_at'].split('T')[0]
    else:
        close_date = None
    dict_test = {
            "coords": f"{review['lat']},{review['lng']}",
            "status": review['status'],
            "summary": review['summary'],
            "description": review['description'],
            "open_date": review['created_at'].split('T')[0],
            "close_date": close_date
    }
    actions.append(dict_test)

insert_data_elasticsearch(logger, elastic_host, elastic_user, elastic_pass, index_name, actions)



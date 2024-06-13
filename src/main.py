import os

from projectutils.api_utils import get_data_api
from util.variables import logger
from projectutils.elastic_utils import insert_data_elasticsearch
from projectutils.execution_utils import execution


def main():
    # Update fact sales

    headers = dict(accept='application/json')
    url_name = 'Zaragoza API'
    url = 'https://www.zaragoza.es/sede/servicio/urbanismo-infraestructuras/equipamiento/parada-taxi/itinerantes?rf=html&srsname=wgs84&start=0&rows=3000&distance=500'
    index_name = "zaragoza-taxi"

    data = get_data_api(logger, url_name, url, headers=headers)

    actions = []

    for review in data['result']:
        # Están al revés las coordenadas
        coordinates = review['geometry']['coordinates'][::-1]
        coordinates_str = ",".join(str(i) for i in coordinates)
        dict_test = {
                "coords": coordinates_str,
                "estado": review['estado'],
                "id": review['id']
            }

        actions.append(dict_test)

    elastic_user = os.getenv('elastic_user')
    elastic_pass = os.getenv('elastic_pass')
    elastic_host = os.getenv('elastic_host')

    insert_data_elasticsearch(logger, elastic_host, elastic_user, elastic_pass, index_name, actions)


if __name__ == '__main__':
    execution(logger, main, 'Zaragoza API example')

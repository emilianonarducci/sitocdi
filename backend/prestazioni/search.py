from opensearchpy import OpenSearch
from django.conf import settings

INDEX_NAME = "prestazioni"

def get_client():
    return OpenSearch(settings.OPENSEARCH_URL)


def create_index():
    client = get_client()
    if client.indices.exists(index=INDEX_NAME):
        return

    client.indices.create(
        index=INDEX_NAME,
        body={
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "nome": {"type": "text", "analyzer": "italian"},
                    "codice": {"type": "keyword"},
                    "branca": {"type": "keyword"},
                    "descrizione": {"type": "text", "analyzer": "italian"},
                    "prezzo_solvente": {"type": "float"},
                    "strutture": {"type": "text", "analyzer": "italian"},
                    "medici": {"type": "text", "analyzer": "italian"},
                    "fondi": {"type": "keyword"},
                    "attiva": {"type": "boolean"},
                }
            }
        },
    )


def index_prestazione(prestazione):
    client = get_client()
    create_index()
    client.index(
        index=INDEX_NAME,
        id=prestazione.id,
        body={
            "id": prestazione.id,
            "nome": prestazione.nome,
            "codice": prestazione.codice,
            "branca": prestazione.branca,
            "descrizione": prestazione.descrizione,
            "prezzo_solvente": float(prestazione.prezzo_solvente) if prestazione.prezzo_solvente else None,
            "strutture": [s.nome for s in prestazione.strutture.all()],
            "medici": [m.nome_completo for m in prestazione.medici.all()],
            "fondi": [f.nome for f in prestazione.fondi.all()],
            "attiva": prestazione.attiva,
        },
    )


def delete_prestazione(prestazione_id):
    client = get_client()
    if client.indices.exists(index=INDEX_NAME):
        client.delete(index=INDEX_NAME, id=prestazione_id, ignore=[404])


def search_prestazioni(query, branca=None, fondo=None, struttura=None):
    client = get_client()

    must = [
        {
            "multi_match": {
                "query": query,
                "fields": ["nome^5", "descrizione^2"],
                "operator": "and",
                "fuzziness": 1,
                "prefix_length": 2,
            }
        }
    ]

    filters = [{"term": {"attiva": True}}]

    if branca:
        filters.append({"term": {"branca": branca}})

    if fondo:
        filters.append({"term": {"fondi": fondo}})

    if struttura:
        filters.append({"match": {"strutture": struttura}})

    response = client.search(
        index=INDEX_NAME,
        body={
            "query": {
                "bool": {
                    "must": must,
                    "filter": filters,
                }
            }
        },
    )

    return [hit["_source"] for hit in response["hits"]["hits"]]

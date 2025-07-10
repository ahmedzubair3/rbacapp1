from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(
    "http://elasticsearch:9200"
)

index_name = "rbcapp1-status"

def insert_to_elasticsearch(doc):
    doc["@timestamp"] = datetime.utcnow().isoformat()
    es.index(index=index_name, document=doc)

def get_all_services_status():
    """
    Get the most recent status for each service and determine the overall app status.
    """
    query = {
        "size": 0,
        "aggs": {
            "by_service": {
                "terms": {"field": "service_name.keyword"},
                "aggs": {
                    "latest_status": {
                        "top_hits": {
                            "size": 1,
                            "sort": [{"@timestamp": {"order": "desc"}}],
                            "_source": {"includes": ["service_status"]}
                        }
                    }
                }
            }
        }
    }

    res = es.search(index=index_name, body=query)
    app_status = "UP"
    result = {}

    for bucket in res["aggregations"]["by_service"]["buckets"]:
        service = bucket["key"]
        status = bucket["latest_status"]["hits"]["hits"][0]["_source"]["service_status"]
        result[service] = status
        if status == "DOWN":
            app_status = "DOWN"

    result["rbcapp1"] = app_status
    return result

def get_service_status(service):
    """
    Get the most recent status of a specific service.
    """
    query = {
        "query": {
            "match": {"service_name": service}
        },
        "sort": [{"@timestamp": {"order": "desc"}}],
        "size": 1
    }

    res = es.search(index=index_name, body=query)
    if res["hits"]["hits"]:
        return res["hits"]["hits"][0]["_source"]["service_status"]
    return "UNKNOWN"

from elasticsearch import Elasticsearch, helpers
import json

# by default we connect to localhost:9200
es = Elasticsearch()
# es = Elasticsearch([{'host':'localhost', 'port': 9200}])

# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.create(index='products', ignore=400)

def importData(Path):
    index = 0
    doc = []
    with open(Path, mode='r') as f2:
        for line in f2:
            index += 1
            # print(line)
            doc.append(json.loads(line))
            if index % 1000 == 0:
                helpers.bulk(es, doc, index='products', doc_type='_doc', request_timeout=200)
                doc = []
                print(index)
                # if index == 100000:break

importData('./archive/test.json') #import test data
# importData('./archive/train.json') #



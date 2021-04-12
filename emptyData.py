from elasticsearch import Elasticsearch

es = Elasticsearch()

delete_by_all = {"query":{"match_all":{}}}
result = es.delete_by_query(index="products", body={"query":{"match_all": {}}}, doc_type="_doc")
print(result)

#delet index
# es.delete(index='products', doc_type='_doc')
import time

from elasticsearch import Elasticsearch
import json
import  pickle


def search(query,label = '__label__1'):
    query_contains = {
        "query":{
            "bool":{
                "must":{
                    "match":{
                        "label":label
                    }
                },
                "should":[
                    {"match":{"review":query}}
                ],
                "minimum_should_match": 1,
            }
        }

    }
    es = Elasticsearch()
    res = es.search(index='products', body=query_contains, size=10)

    id = []
    for each in res['hits']['hits'][:10]:
        if each['_source']['id'] not in id:
            id.append(each['_source']['id'])
        # print(each['_source']['id'])
            print(each['_score'],each['_source']['label'])
            print(each['_source']['review'])
    return res


def get_predictions(comment):
    filename = './finalized_model.sav'
    filename2 = './finalized_contVec.sav'
    model = pickle.load(open(filename, 'rb'))
    contVec = pickle.load(open(filename2, 'rb'))
    comment_feature = contVec.transform([comment])
    # print(model.predict(comment_feature))

    return model.predict(comment_feature)[0]

# res = search('Great CD PLAYER','__label__2')
# res = search('Suck CD PLAYER','__label__2')

# r = json.dumps(res, sort_keys=True, indent=4)
# print(r)

if __name__=='__main__':
    query = input('input query: ')
    s_t = time.time()
    label = get_predictions(query)
    search(query,label)
    e_t = time.time()
    print('time cost: ',round(e_t-s_t,2),'s')
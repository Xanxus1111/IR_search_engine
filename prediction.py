import json
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pickle
comment = "I like it!"
def train():
    train_data = []
    for line in open('./archive/test.json', 'r', encoding='utf8'):
        train_data.append(json.loads(line))
    train_set, test_set = train_test_split(train_data, test_size=0.3, random_state=42)
    train_label = [data['label'] for data in train_set]
    test_label = [data['label'] for data in test_set]
    train_set = [data['review'] for data in train_set]
    test_set = [data['review'] for data in test_set]
    contVec = CountVectorizer()
    train_feature = contVec.fit_transform(train_set)
    print("Finish contVec")
    model = LogisticRegression(solver='liblinear')
    model.fit(train_feature, train_label)
    print("Finish Train")
    #test_feature = contVec.transform(test_set)
    # predictions = model.predict(test_feature)
    # print('accuracy:', accuracy_score(test_label, predictions) * 100)
    #comment_feature = contVec.transform([comment])
    # save the model to disk
    filename = './finalized_model.sav'
    filename2 = './finalized_contVec.sav'

    pickle.dump(model, open(filename, 'wb'))
    pickle.dump(contVec, open(filename2, 'wb'))
    return model,contVec
# model,contVec = train()
train()



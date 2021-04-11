import json
dict_data={}

path = './archive/'
trainFile = 'train.ft.txt'
testFile = 'test.ft.txt'
tarinDataset = 'train.json'
testDataset = 'test.json'


def preprocess(inputPath,outPath):
    index = 0
    json_str = ''
    limitNum = 20  # set the limit of how many you want to get from the dataset if you want

    with open(inputPath,'r')as df:
        for line in df:
            index += 1
            dataDict = {}
            dataDict['id'] = index
            dataDict['label'] = line.split(' ',1)[0]
            dataDict['review'] = line.split(' ',1)[1]
            json_str = json_str + 'for_split_label'+json.dumps(dataDict)
            # if index == limitNum:  # set the limit of how many you want to get from the dataset if you want
            #     break


    with open(outPath,"w") as f:
        for each in json_str.split('for_split_label'):
            if each !='':
                f.write(each+'\n')

preprocess(path+trainFile,path+tarinDataset)
preprocess(path+testFile,path+testDataset)




















# IR_search_engine QMUL group w

![image](https://user-images.githubusercontent.com/15157064/114306134-75502980-9b0d-11eb-817d-b21c7b3c01d7.png)

Need to pay attention to the file path. Modify the file path if needed.

Put the file and dataset folder under the same folder and run it 
```
python preprocess.py
```
## Create index and import data to elastic search engine

**I found that when I import data many times, elastic would not delete the repeated data. So just run this file one time**

After start elastic search engine, run createIndex.py
Creat index and import data to elastic search engine.
```
python creatIndex.py
```

## Empty data
```
python emptyData.py
```

## Train model
```
python prediction.py
```

## Begin to search
```
python search.py
```
![image](https://user-images.githubusercontent.com/15157064/114917964-22ea7200-9e59-11eb-8313-66aa1f17c498.png)
![image](https://user-images.githubusercontent.com/15157064/114917975-24b43580-9e59-11eb-8c80-02bf23b9705b.png)

## Runing flask
```
python searchWebsite.py
```

![image](https://user-images.githubusercontent.com/15157064/114984856-b73dee80-9ec4-11eb-99aa-4402b6d94aee.png)




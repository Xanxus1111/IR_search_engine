from flask import Flask
from flask import render_template  # 渲染
from flask import request
app = Flask(__name__)

import search

@app.route('/')  # 主页地址,“装饰器”
def reviews():
    the_news = {
        'XXX1': '1',
        'XXX2': '2',
        'XXX3': '3',
        'XXX4': '4',
    }
    context = {
        'title': 'Review Search Engine',
        'the_news': the_news,
    }
    return render_template('index.html', context=context)  #


@app.route('/search_method', methods=['GET', 'POST'])
def search_method():
    keyword = request.form['keyword']
    label = search.get_predictions(keyword)
    result = search.search(keyword,label)

    the_news = result
    context = {
        'title': 'Review Search Engine',
        'the_reviews': the_news,
    }
    return render_template('index.html', context=context)  #

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)  #

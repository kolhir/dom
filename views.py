from dom import app
from flask import render_template, request
from dom  import u2_views, u3_views
from copy import deepcopy

bt_dict = {
    "bt1": {
        "alarm_off":0,
        "open":0,
        "close":0,
        "reset":0
    },
    "bt1_status":{
        "flood":0,
        "valve":0,
        "alarm":0
    },
    "bt1_status_convert":{
        "flood":{
        0:"Нет",
        1:"Есть"
        },
        "valve":{
        0:"Закрыт",
        1:"Открыт",
        2:"Не исправен"
        },
        "alarm":{
        0:"Выключена",
        1:"Включена"
        },
    },
}

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    data = deepcopy(bt_dict["bt1_status"])
    for i in bt_dict["bt1_status"]:
        data[i] = bt_dict["bt1_status_convert"][i][data[i]]
    return render_template("index.html",
        data = data
        )

@app.route('/bt1')
def bt1_get():
    res = ""
    print(42)
    for i in bt_dict["bt1"]:
        res = res + str(bt_dict["bt1"][i])
        bt_dict["bt1"][i] = 0
    return res



@app.route('/u1')
def u1():
    data = deepcopy(bt_dict["bt1_status"])
    for i in data:
        data[i] = bt_dict["bt1_status_convert"][i][data[i]]
    return render_template("u1.html",
        data = data
        )

@app.route('/u1/alarm_off')
@app.route('/u1/open')
@app.route('/u1/close')
@app.route('/u1/reset')
def u1_but():
    global bt_dict
    key = request.url.split("/")[4]
    for i in bt_dict["bt1"]:
        if i == key:
            bt_dict["bt1"][i] = 1
        else:
            bt_dict["bt1"][i] = 0
    print(bt_dict["bt1"])
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h4>Сигнал <b><i>''' + key + '''</i></b> был отправлен!</h4>
    <a href="/u1" class="green">Вернуться назад</a>
  </body>
</html>
'''

import json

@app.route("/bt1", methods = ['POST'])
def ajax_bron():
    if request.method == 'POST':
        answer=json.loads(request.get_data())
        global bt_dict
        for key in answer:
            bt_dict["bt1_status"][key]=int(answer[key])
        return "hi"

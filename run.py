#!/home/kolhir/dev/flaskenv/robinlt/bin/python3
from flask import Flask
from flask import render_template, request
import views
app = Flask(__name__)
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
        3:"Не исправен"
        },
        "alarm":{
        0:"Выключена",
        1:"Включена"
        },
    }

}

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    data = deepcopy(bt_dict["bt1_status"])
    for i in data:
        data[i] = bt_dict["bt1_status_convert"][i][data[i]]
    return render_template("index.html",
        data = data
        )

@app.route('/bt1')
def bt1_get():
    res = ""
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

@app.route('/u2')
def u2():
    return render_template("u2.html")

@app.route('/u3')
def u3():
    return render_template("u3.html")

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

@app.route("/", methods = ['POST'])
def ajax_bron():
    return json.dumps(200)


from somewhere import ip
# app.debug = True
if __name__ == "__main__":
    app.run(ip, debug = True)


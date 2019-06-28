from dom import app
from flask import render_template, request
from copy import deepcopy

bt2_dict = {
    "bt2": {
        "alarm_off":0,
        "open":0,
        "close":0,
        "reset":0
    },
    "bt2_status":{
        "leak":0,
        "valve":0,
        "alarm":0,
        "ppm":0
    },
    "bt2_status_convert":{
        "leak":{
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
    }
}


@app.route('/bt2')
def bt2_get():
    res = ""
    print(43)
    for i in bt2_dict["bt2"]:
        res = res + str(bt2_dict["bt2"][i])
        bt2_dict["bt2"][i] = 0
    return res

@app.route('/u2')
def u2():
    data = deepcopy(bt2_dict["bt2_status"])
    for i in data:
    	if i != "ppm":
        	data[i] = bt2_dict["bt2_status_convert"][i][data[i]]
    return render_template("u2.html",
        data = data
        )

@app.route('/u2/alarm_off')
@app.route('/u2/open')
@app.route('/u2/close')
@app.route('/u2/reset')
def u2_but():
    global bt2_dict
    key = request.url.split("/")[4]
    for i in bt2_dict["bt2"]:
        if i == key:
            bt2_dict["bt2"][i] = 1
        else:
            bt2_dict["bt2"][i] = 0
    print(bt2_dict["bt2"])
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

from dom import app
from flask import render_template, request
from copy import deepcopy
import json

bt3_dict = {
    "bt3": {
        "on":0,
        "off":0,
        "onsup":0,
        "sup":0
    },
    "bt3_status":{
        "status":"off",
        "temp":0,
        "time":0,
    },
    "bt3_status_convert":{
        "status":{
        "on":"Включен",
        "off":"Выключен",
        "onsup":"Включен и поддерживает",
        "sup":"Поддерживает"
        },
    }
}


@app.route('/bt3')
def bt3_get():
    res = ""
    print(43)
    for i in bt3_dict["bt3"]:
        res = res + str(bt3_dict["bt3"][i])
        bt3_dict["bt3"][i] = 0
    return res

@app.route('/u3')
def u3():
    data = deepcopy(bt3_dict["bt3_status"])
    data["status"] = bt3_dict["bt3_status_convert"]["status"][data["status"]]
    return render_template("u3.html",
        data = data
        )

@app.route('/u3/post', methods=['POST'])
def u3_but():
    global bt3_dict
    status = ""
    bt3_dict["bt3_status"]["time"] = request.form["time"]
    bt3_dict["bt3_status"]["temp"] = request.form["temp"]
    for i in bt3_dict["bt3"]:
        if i in request.form:
            bt3_dict["bt3_status"]["status"] = i
            bt3_dict["bt3"][i] = 1
    print(bt3_dict)
    

    data = deepcopy(bt3_dict["bt3_status"])
    data["status"] = bt3_dict["bt3_status_convert"]["status"][data["status"]]
    return render_template("u3.html",
        data = data
        )

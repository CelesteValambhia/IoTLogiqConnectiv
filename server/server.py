import json
from flask import Flask, jsonify, request
from Sensors.TemperatureSensor import TemperatureSensor
from Sensors.BrightnessSensor import BrightnessSensor
from Sensors.Seasons import Seasons, current_season
from datetime import datetime
from Sensors.InitializedActuators import lamp
from Sensors.InitializedActuators import thermostat
from Sensors.InitializedActuators import ac

app = Flask(__name__)

@app.route('/testapi')
def index():
    try:
        pass
    except Exception as exp:
        return str(exp)
    return jsonify({'name': 'IoTLogiqConnectiv',
                    'email': 'celeste.valambhia@gmail.com'})


@app.route('/temperature', methods=['POST'])
def post_temperature():
    try:
        ts = TemperatureSensor(25, 2, 0, 35)
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        message = {
            "type-id": "de.uni-stuttgart.iaas.sc." + ts.sensorType,
            "instance-id": ts.instanceID,
            "timestamp": dt,
            "value": {ts.unit: ts.sense()}
        }
        # jmsg = json.dumps(message, indent=4)
        jmsg = jsonify(message)
        # print(jmsg)
        return jmsg
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})

@app.route('/seasons', methods=['POST'])
def post_seasons():
    try:
        currentMonth = datetime.today().month
        # print(current_season(currentMonth))
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        message = {
            "type-id": "de.uni-stuttgart.iaas.sc." + Seasons.sensorType,
            "instance-id": Seasons.instanceID,
            "timestamp": dt,
            "value": {Seasons.unit: current_season(currentMonth)}
        }
        jmsg = jsonify(message)
        # print(jmsg)
        return jmsg
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})

@app.route('/brightness', methods=['POST'])
def post_brightness():
    try:
        br = BrightnessSensor(30, 2, 0, 100)
        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        message = {
            "type-id": "de.uni-stuttgart.iaas.sc." + br.sensorType,
            "instance-id": br.instanceID,
            "timestamp": dt,
            "value": {br.unit: br.sense()}
        }
        # jmsg = json.dumps(message, indent=4)
        jmsg = jsonify(message)
        # print(jmsg)
        return jmsg
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})


@app.route('/luminance', methods=['GET', 'POST'])
def get_luminance():
    try:
        if request.method == 'GET':
            data = {'luma': lamp.get()}
            return jsonify(data)
        elif request.method == 'POST':
            data = request.json
            lamp.set(value=data['lamp_lumaval'])
            return jsonify({
                "status": "OK",
                "message": "Value set successfully",
                **dict(data)
            })
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})

@app.route('/thermostat', methods=['GET', 'POST'])
def get_thermostattemp():
    try:
        if request.method == 'GET':  # Try something like wait until get request doesn't come
            data = {'status': thermostat.getstatus(),
                    'temperature': thermostat.get()}
            return jsonify(data)
        elif request.method == 'POST':
            data = request.json
            thermostat.set(value=data['temperature'])
            thermostat.setstatus(status=data['status'])
            return jsonify({
                "status": "OK",
                "message": "Value set successfully",
                **dict(data)
            })
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})

@app.route('/ac', methods=['GET', 'POST'])
def get_actemp():
    try:
        if request.method == 'GET':  # Try something like wait until get request doesn't come
            data = {'status': ac.getstatus(),
                    'temperature': ac.get()}
            return jsonify(data)
        elif request.method == 'POST':
            data = request.json
            ac.set(value=data['temperature'])
            ac.setstatus(status=data['status'])
            return jsonify({
                "status": "OK",
                "message": "Value set successfully",
                **dict(data)
            })
    except Exception as exp:
        return str(exp)
        # return jsonify({'error': 'data not found'})


app.run(host="0.0.0.0", debug=True)

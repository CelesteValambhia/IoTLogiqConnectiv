"""
Author: Celeste Valambhia
Description: API's to retrive sensor values
"""

from subprocess import check_output, CalledProcessError
import json
import requests


def readBrightness(log):
    try:
        httpResponse = requests.post('http://192.168.0.102:5000/brightness?value')
        json_load = httpResponse.json()
        # print(json_load['value']['lux'])
        return json_load['value']['lux']
    except CalledProcessError as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False

def readLampLuminance(log):
    try:
        httpResponse = requests.get('http://192.168.0.102:5000/luminance')
        json_load = httpResponse.json()
        # print(json_load['luma'])
        return json_load['luma']
    except CalledProcessError as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False

def readTemperature(log):
    try:
        httpResponse = requests.post('http://192.168.0.102:5000/temperature')
        json_load = httpResponse.json()
        # print(json_load['value']['celsius'])
        return json_load['value']['celsius']
    except CalledProcessError as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False

def readThermostatTemp(log):
    try:
        httpResponse = requests.get('http://192.168.0.102:5000/thermostat')
        json_load = httpResponse.json()
        # print(json_load['luma'])
        return json_load['temperature']
    except CalledProcessError as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False

def readSeasons(log):
    try:
        httpResponse = requests.post('http://192.168.0.102:5000/seasons')
        json_load = httpResponse.json()
        # print(json_load['value']['None'])
        return json_load['value']['None']
    except CalledProcessError as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=" + str(e))
        return False


'''
def readBrightness():
    try:
        query = "curl --silent --insecure -X POST -H \'Content-Type: application/json\' http://localhost:5000/brightness?value"
        httpResponse = check_output(query, shell=True)
        json_load = (json.loads(httpResponse))
        print(json_load['value']['lux'])
        return json_load['value']['lux']
    except CalledProcessError as e:
        print(e)
        return e
    except Exception as e:
        print(e)
        return e
'''

'''
if __name__ == "__main__":
    # bright = readBrightness()
    # temp = readTemperature()
    luma = readLampLuminance()
    print(type(luma))
'''
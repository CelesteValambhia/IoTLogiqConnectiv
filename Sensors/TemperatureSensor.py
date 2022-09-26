import time
from datetime import datetime
import json
from random import random

class TemperatureSensor:
    sensorType = "temperature"
    instanceID = "32kd403ks"
    unit = "celsius"

    def __init__(self, averageTemperature, temperatureVariation, minTemperature, maxTemperature):
        self.averageTemperature = averageTemperature
        self.temperatureVariation = temperatureVariation
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature
        self.value = 0.0

    def sense(self):
        # self.value = self.value + self.simpleRandom()
        self.value = self.complexRandom()
        return self.value

    def simpleRandom(self):
        value = self.minTemperature + (random() * (self.maxTemperature - self.minTemperature))
        return value

    def complexRandom(self):
        value = self.averageTemperature * (1 + ((self.temperatureVariation / 100) * (3 * random() - 1)))
        value = max(value, self.minTemperature)
        value = min(value, self.maxTemperature)
        return value


class Simulator:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        ts = TemperatureSensor(25, 2, 0, 35)
        while True:
            dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            message = {
                "type-id": "de.uni-stuttgart.iaas.sc." + ts.sensorType,
                "instance-id": ts.instanceID,
                "timestamp": dt,
                "value": {ts.unit: ts.sense()}
            }
            jmsg = json.dumps(message, indent=4)
            print(jmsg)
            time.sleep(self.interval)


s = Simulator(5)
s.start()

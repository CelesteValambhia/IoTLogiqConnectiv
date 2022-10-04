import time
from datetime import datetime
import json
from random import random

class BrightnessSensor:
    sensorType = "luminance"
    instanceID = "345gf9erf"
    unit = "lux"

    def __init__(self, averageLuminance, luminanceVariation, minLuminance, maxLuminance):
        self.averageLuminance = averageLuminance
        self.luminanceVariation = luminanceVariation
        self.minLuminance = minLuminance
        self.maxLuminance = maxLuminance
        self.value = 0.0

    def sense(self):
        # self.value = self.value + self.simpleRandom()
        self.value = self.complexRandom()
        return self.value

    def simpleRandom(self):
        value = self.minLuminance + (random() * (self.maxLuminance - self.minLuminance))
        return value

    def complexRandom(self):
        value = self.averageLuminance * (1 + ((self.luminanceVariation / 100) * (3 * random() - 1)))
        value = max(value, self.minLuminance)
        value = min(value, self.maxLuminance)
        return value

'''
class Simulator:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        br = BrightnessSensor(60, 2, 0, 100)
        while True:
            dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            message = {
                "type-id": "de.uni-stuttgart.iaas.sc." + br.sensorType,
                "instance-id": br.instanceID,
                "timestamp": dt,
                "value": {br.unit: br.sense()}
            }
            jmsg = json.dumps(message, indent=4)
            print(jmsg)
            time.sleep(self.interval)


s = Simulator(5)
s.start()
'''
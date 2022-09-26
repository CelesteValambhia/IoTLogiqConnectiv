import time
from datetime import datetime
import json
from Sensors.smulatediot import TemperatureSensor


class Simulator:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        ts = TemperatureSensor(20, 10, 16, 30)
        while True:
            dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
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

import time
from datetime import datetime
import json


def current_season(current_month):
    if current_month in range(4, 10):
        season = str("Summer")
    else:
        season = str("Winter")
    return season

'''
currentMonth = datetime.today().month
print(current_season(currentMonth))
'''
class Seasons:
    sensorType = "seasons"
    instanceID = "69e73lh89"
    unit = "None"

'''
class Simulator:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        while True:
            currentMonth = datetime.today().month
            # print(current_season(currentMonth))
            dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            message = {
                "type-id": "de.uni-stuttgart.iaas.sc." + Seasons.sensorType,
                "instance-id": Seasons.instanceID,
                "timestamp": dt,
                "value": {Seasons.unit: current_season(currentMonth)}
            }
            jmsg = json.dumps(message, indent=4)
            print(jmsg)
            time.sleep(self.interval)


s = Simulator(60)
s.start()
'''

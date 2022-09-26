from solver import *

log = IoTLogger()

def SolveComfortQuery(message):
    # print(message)
    if "Set_Room_Temp_Comfortable" in message:
        try:
            setcom = SetRoomTempComfortable(log)
            return "Room Temperature Set Comfortable!"
        except Exception as e:
            print("Temp Cannot be set")
            log.log_error(f"AI Planner has encountered an error!")
            print(e)
            return False

def ClassifyInput(message):
    msg = message.text.split("_")
    if "Comfortable" in msg:
        solve = SolveComfortQuery(str(message))
        return solve

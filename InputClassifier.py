from AI_Planner.logger import *
from ComfortAnalyserSolver import *

log = IoTLogger()


def ClassifyInput(message):
    log.log_info("Func=" + __name__ + " : " + "Log=message: " + message.text)
    msg = message.text.split("_")
    # print(msg)
    if "Comfortable" in msg:
        solve = SolveComfortQuery(str(message))
        return solve
    else:
        solve = SolveInstructions(message)
        return solve


def SolveInstructions(message):
    # print(message)
    message = message.text.split(" ")
    # print(message.text)

    if "Get_Room_Brightness" in message[0]:
        brightness = readBrightness(log)
        if not brightness:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read current brightness")
            return "Cannot get brightness value"
        log.log_info("Func=" + __name__ + " : " + "Log=Current brightness is " + str(brightness) + " luma.")
        return "Current brightness is " + str(brightness) + " luma."

    if "Get_Room_Temperature" in message[0]:
        temperature = readTemperature(log)
        if not temperature:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read current temperature")
            return "Cannot get temperature value"
        log.log_info("Func=" + __name__ + " : " + "Log=Current temperature is " + str(temperature) + " degree celsius.")
        return "Current temperature is " + str(temperature) + " degree celsius."

    if "Get_Season" in message[0]:
        season = readSeasons(log)
        if not season:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot get season")
            return "Cannot get current season"
        log.log_info("Func=" + __name__ + " : " + "Log=Current season is " + str(season))
        return "Current season is " + str(season)

    if "Set_Lamp_Luminance" in message[0]:
        log.log_info("Func=" + __name__ + " : " + "Log=Setting luminance to " + str(message[1]) + " luma.")
        value = int(message[1])
        if value in range(0, 101):
            try:
                requests.post("http://localhost:5000/luminance", json={"lamp_lumaval": value})
                log.log_info("Func=" + __name__ + " : " + "Log=Luminance set to " + str(value) + " luma.")
                return "Luminance set to " + str(value) + " luma."
            except Exception as e:
                log.log_error("Func=" + __name__ + " : " + "Log=Luminance cannot be set.")
                return "Luminance cannot be set. Error in server."
        else:
            log.log_error("Func=" + __name__ + " : " + "Log=Invalid Luminance value")
            return "Invalid luminance value. Range is 0-100 luma. Please try again!"

    if "Set_Thermostat_Temperature" in message[0]:
        log.log_info("Func=" + __name__ + " : " + "Log=Setting temperature to " + str(message[1]) + " degree celsius.")
        value = int(message[1])
        if value in range(17, 31):
            try:
                requests.post("http://localhost:5000/thermostat", json={"temperature": value})
                log.log_info("Func=" + __name__ + " : " + "Log=Thermostat temperature set to " + str(value) + " degree "
                                                                                                              "celsius.")
                return "Temperature set to " + str(value) + " degree celsius."
            except Exception as e:
                log.log_error("Func=" + __name__ + " : " + "Log=Thermostat temperature cannot be set.")
                return "Thermostat temperature cannot be set. Error in server."
        else:
            log.log_error("Func=" + __name__ + " : " + "Log=Invalid temperature value")
            return "Invalid temperature value. Range is 18-30 degree celsius. Please try again!"

    if "Get_Lamp_Luminance" in message[0]:
        luma = readLampLuminance(log)
        if not luma:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read current lamp luminance")
            return "Cannot get luminance value"
        log.log_info("Func=" + __name__ + " : " + "Log=Current lamp luminance is " + str(luma) + " luma.")
        return "Current lamp luminance is " + str(luma) + " luma."

    if "Get_Thermostat_Temperature" in message[0]:
        thermotemp = readThermostatTemp(log)
        if not thermotemp:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read current thermostat temperature")
            return "Cannot read current thermostat temperature"
        log.log_info("Func=" + __name__ + " : " + "Log=Current thermostat temperature is " + str(
            thermotemp) + " degree celsius.")
        return "Current thermostat temperature is " + str(thermotemp) + " degree celsius."

    elif (str(message[0]) != "Get_Room_Temperature") or (str(message[0]) != "Get_Lamp_Luminance") or (
            str(message[0]) != "Get_Room_Brightness") or (str(message[0]) != "Get_Season") or (
            str(message[0]) != "Set_Thermostat_Temperature") or (str(message[0]) != "Get_Thermostat_Temperature") or (
            str(message[0]) != "Set_Lamp_Luminance"):
        # print(str(message[0]))
        log.log_error("Func=" + __name__ + " : " + "Log=Invalid Instruction")
        return "Invalid Instruction"


def SolveComfortQuery(message):
    # print(message)
    if "Set_Room_Temp_Comfortable" in message:
        try:
            if not SetRoomTempComfortable(log):
                return "Room Temperature Cannot be Set Comfortable!"
            return "Room Temperature Set Comfortable!"
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=Temperature cannot be set.")
            log.log_error(f"AI Planner has encountered an error!")
            print(e)
            return "Room Temperature Cannot be Set Comfortable!"

    if "Set_Room_Light_Comfortable" in message:
        try:
            if not SetRoomLightComfortable(log):
                return "Room Lightning Cannot be Set Comfortable!"
            return "Room Lightning Set Comfortable!"
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=Luminance cannot be set.")
            log.log_error(f"AI Planner has encountered an error!")
            print(e)
            return "Room Lightning Cannot be Set Comfortable!"

    if "Set_Room_Comfortable" in message:
        try:
            if not SetRoomLightComfortable(log):
                return "Room Lightning Cannot be Set Comfortable!"
            if not SetRoomTempComfortable(log):
                return "Room Temperature Cannot be Set Comfortable!"
            return "Room Set Comfortable!"
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=Comfort cannot be set.")
            log.log_error(f"AI Planner has encountered an error!")
            print(e)
            return "Room Cannot be Set Comfortable"

    else:
        log.log_error("Func=" + __name__ + " : " + "Log=Invalid Instruction")
        return "Invalid Instruction"

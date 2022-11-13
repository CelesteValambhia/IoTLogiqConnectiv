from AI_Planner.logger import *
from ComfortAnalyserSolver import *
from ErrorNotifier import *
from EnergyOptimiserSolver import *

log = IoTLogger()


def ClassifyInput(message):
    log.log_info("Func=" + __name__ + " : " + "Log=message: " + message.text)
    msg = message.text.split("_")
    # print(msg)
    if "Comfortable" in msg:
        solve = SolveComfortQuery(str(message))
        return solve
    elif "Optimise" in msg:
        solve = SolveOptimiserQuery(message)
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
            SendEmail(log)
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
        status = readThermostatStatus(log)
        if value in range(17, 51) and status == "On":
            try:
                requests.post("http://localhost:5000/thermostat", json={"temperature": value})
                log.log_info("Func=" + __name__ + " : " + "Log=Thermostat temperature set to " + str(value) + " degree "
                                                                                                              "celsius.")
                return "Temperature set to " + str(value) + " degree celsius."
            except Exception as e:
                log.log_error("Func=" + __name__ + " : " + "Log=Thermostat temperature cannot be set.")
                return "Thermostat temperature cannot be set. Error in server."
        elif status == "Off":
            log.log_error("Func=" + __name__ + " : " + "Log=Thermostat temperature cannot be set. Thermostat is Off.")
            return "Thermostat temperature cannot be set. Thermostat is Off."
        else:
            log.log_error("Func=" + __name__ + " : " + "Log=Invalid temperature value")
            return "Invalid temperature value. Range is 18-50 degree celsius. Please try again!"

    if "Set_AC_Temperature" in message[0]:
        log.log_info("Func=" + __name__ + " : " + "Log=Setting temperature to " + str(message[1]) + " degree celsius.")
        value = int(message[1])
        status = readACStatus(log)
        if value in range(17, 31) and status == "On":
            try:
                requests.post("http://localhost:5000/ac", json={"temperature": value})
                log.log_info("Func=" + __name__ + " : " + "Log=AC temperature set to " + str(value) + " degree celsius.")
                return "Temperature set to " + str(value) + " degree celsius."
            except Exception as e:
                log.log_error("Func=" + __name__ + " : " + "Log=AC temperature cannot be set.")
                return "AC temperature cannot be set. Error in server."
        elif status == "Off":
            log.log_error("Func=" + __name__ + " : " + "Log=AC temperature cannot be set. AC is Off.")
            return "AC temperature cannot be set. AC is Off."
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

    if "Get_AC_Temperature" in message[0]:
        actemp = readACTemp(log)
        if not actemp:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read current AC temperature")
            return "Cannot read current AC temperature"
        log.log_info("Func=" + __name__ + " : " + "Log=Current AC temperature is " + str(
            actemp) + " degree celsius.")
        return "Current AC temperature is " + str(actemp) + " degree celsius."

    if "Get_AC_Status" in message[0]:
        status = readACStatus(log)
        log.log_info("Func=" + __name__ + " : " + "Log=AC status is " + status)
        return "AC status is " + status

    if "Get_Thermostat_Status" in message[0]:
        status = readThermostatStatus(log)
        log.log_info("Func=" + __name__ + " : " + "Log=Thermostat status is " + status)
        return "Thermostat status is " + status

    if "Set_Thermostat_Status" in message[0]:
        log.log_info("Func=" + __name__ + " : " + "Log=Setting thermostat " + str(message[1]))
        status = str(message[1])
        try:
            requests.post("http://localhost:5000/thermostat", json={"status": status, "temperature": 0})
            return "Setting thermostat " + str(message[1])
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=Thermostat status cannot be set.")
            return "Thermostat status cannot be set. Error in server."

    if "Set_AC_Status" in message[0]:
        log.log_info("Func=" + __name__ + " : " + "Log=Setting AC " + str(message[1]))
        status = str(message[1])
        try:
            requests.post("http://localhost:5000/ac", json={"status": status, "temperature": 0})
            return "Setting AC " + str(message[1])
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=AC status cannot be set.")
            return "AC status cannot be set. Error in server."

    elif (str(message[0]) != "Get_Room_Temperature") or (str(message[0]) != "Get_Lamp_Luminance") or (
            str(message[0]) != "Get_Room_Brightness") or (str(message[0]) != "Get_Season") or (
            str(message[0]) != "Set_Thermostat_Temperature") or (str(message[0]) != "Set_AC_Temperature") or (
            str(message[0]) != "Get_Thermostat_Temperature") or (str(message[0]) != "Set_Lamp_Luminance") or (
            str(message[0]) != "Get_AC_Temperature") or (str(message[0]) != "Get_Thermostat_Status") or (
            str(message[0]) != "Get_AC_Status") or (str(message[0]) != "Set_Thermostat_Status") or (
            str(message[0]) != "Set_AC_Status"):
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


def SolveOptimiserQuery(message):
    # print(message)
    message = message.text.split(" ")
    # print(message.text)

    if "Optimise_Room" in message[0]:
        try:
            if not OptimiseRoom(log):
                return "Room Cannot be Optimised!"
            return "Room Optimised!"
        except Exception as e:
            log.log_error("Func=" + __name__ + " : " + "Log=Room Cannot be Optimised!")
            log.log_error(f"AI Planner has encountered an error!")
            print(e)
            return "Room Cannot be Optimised!"
    else:
        log.log_error("Func=" + __name__ + " : " + "Log=Invalid Instruction")
        return "Invalid Instruction"

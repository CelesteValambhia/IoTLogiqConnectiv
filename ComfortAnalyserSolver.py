from AI_Planner.pddl import *
from readSensorValues import *
from setGoal import *
from Sensors.InitializedActuators import lamp
import requests
import time
import re


comfort_temperature_summer = (20.00, 30.00)
comfort_temperature_winter = (15.00, 20.00)
comfort_luminance = (50.00, 70.00)

plan_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\plan.txt")
problem_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\Comfort_Analyser_Problem.pddl")

def SetRoomLightComfortable(log):

    solver = Solver(
        domain_file="Comfort_Analyser_Domain.pddl",
        problem_file="Comfort_Analyser_Problem.pddl",
        solution_filename="plan.txt",
        solver_uri="http://solver.planning.domains/solve",
    )
    try:
        # read brightness
        brightness = readBrightness(log)
        # read lamp luminance value
        lamplum = readLampLuminance(log)
        if not brightness:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read brightness")
            return False
        else:
            log.log_info("Func=" + __name__ + " : " + "Log=Brightness: " + str(brightness))

            # If brightness is less
            if brightness <= comfort_luminance[0]:
                log.log_info("Func=" + __name__ + " : " + "Log=Brightness is low.")
                if not setLuminanceHighGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_increase_brightness" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_increase_brightness")
                    lmvalue = (comfort_luminance[0] - brightness) - lamplum
                    if lmvalue < 0:
                        lmvalue = 0
                    setLampValue(log, lmvalue)

            # If brightness is more
            elif brightness >= comfort_luminance[1]:
                log.log_info("Func=" + __name__ + " : " + "Log=Brightness is high.")
                if not setLuminanceLowGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_decrease_brightness" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_decrease_brightness")
                    lmvalue = lamplum - (brightness - comfort_luminance[1])
                    if lmvalue < 0:
                        lmvalue = 0
                    setLampValue(log, lmvalue)

            else:
                log.log_info("Func=" + __name__ + " : " + "Log=Brightness is comfortable!")

            return True

    except Exception as e:
        log.log_error(f"AI Planner has encountered an error!")
        print(e)
        return False

def SetRoomTempComfortable(log):
    solver = Solver(
        domain_file="Comfort_Analyser_Domain.pddl",
        problem_file="Comfort_Analyser_Problem.pddl",
        # problem_template=f"{PDDL_Directory}/problem_template.pddl",
        solution_filename="plan.txt",
        solver_uri="http://solver.planning.domains/solve",
    )
    try:
        season = readSeasons(log)
        if not season:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read seasons")
            return False
        else:
            log.log_info("Func=" + __name__ + " : " + "Log=Season: " + str(season))

        temperature = readTemperature(log)
        if not temperature:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read temperature")
            return False
        else:
            log.log_info("Func=" + __name__ + " : " + "Log=Temperature: " + str(temperature))

        thermostat = readThermostatTemp(log)
        if not thermostat:
            log.log_error("Func=" + __name__ + " : " + "Log=Cannot read thermostat")
            return False
        else:
            log.log_info("Func=" + __name__ + " : " + "Log=Thermostat temperature: " + str(temperature))

        if season == "Summer":
            if temperature <= comfort_temperature_summer[0]:
                log.log_info("Func=" + __name__ + " : " + "Log=Temperature is low.")
                if not setACHighGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_thermostat_off" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_thermostat_off")
                    try:
                        requests.post("http://localhost:5000/thermostat", json={"status": "Off", "temperature": 0})
                        log.log_info("Func=" + __name__ + " : " + "Log=Thermostst is Off.")
                        # return "Setting Thermostat Off"
                    except Exception as e:
                        log.log_error("Func=" + __name__ + " : " + "Log=Thermostat cannot be set off.")
                        # return "Thermostat cannot be set off. Error in server."

                if "action_increasetemperature_summer" in actions:
                    log.log_debug(
                        "Func=" + __name__ + " : " + "Log=Performing action action_increasetemperature_summer")
                    acvalue = 24.00
                    status = readACStatus(log)
                    if status == "On":
                        try:
                            requests.post("http://localhost:5000/ac", json={"temperature": acvalue})
                            log.log_info("Func=" + __name__ + " : " + "Log=AC temperature set to " + str(
                                acvalue) + " degree celsius.")
                            # return "Temperature set to " + str(acvalue) + " degree celsius."
                        except Exception as e:
                            log.log_error("Func=" + __name__ + " : " + "Log=AC temperature cannot be set.")
                            # return "AC temperature cannot be set. Error in server."

            if temperature >= comfort_temperature_summer[1]:
                log.log_info("Func=" + __name__ + " : " + "Log=Temperature is high.")
                if not setACLowGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_thermostat_off" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_thermostat_off")
                    try:
                        requests.post("http://localhost:5000/thermostat", json={"status": "Off", "temperature": 0})
                        log.log_debug("Func=" + __name__ + " : " + "Log=Thermostst is Off.")
                        # return "Setting Thermostat Off"
                    except Exception as e:
                        log.log_error("Func=" + __name__ + " : " + "Log=Thermostat cannot be set off.")
                        # return "Thermostat cannot be set off. Error in server."

                if "action_decreasetemperature_summer" in actions:
                    log.log_debug(
                        "Func=" + __name__ + " : " + "Log=Performing action action_decreasetemperature_summer")
                    acvalue = 18.00
                    status = readACStatus(log)
                    if status == "On":
                        try:
                            requests.post("http://localhost:5000/ac", json={"temperature": acvalue})
                            log.log_info("Func=" + __name__ + " : " + "Log=AC temperature set to " + str(
                                acvalue) + " degree celsius.")
                            # return "Temperature set to " + str(acvalue) + " degree celsius."
                        except Exception as e:
                            log.log_error("Func=" + __name__ + " : " + "Log=AC temperature cannot be set.")
                            # return "AC temperature cannot be set. Error in server."

        if season == "Winter":
            if temperature <= comfort_temperature_winter[0]:
                log.log_info("Func=" + __name__ + " : " + "Log=Temperature is low.")
                if not setThermostatHighGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_ac_off" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_ac_off")
                    try:
                        requests.post("http://localhost:5000/ac", json={"status": "Off", "temperature": 0})
                        log.log_info("Func=" + __name__ + " : " + "Log=AC is Off.")
                        # return "Setting AC Off"
                    except Exception as e:
                        log.log_error("Func=" + __name__ + " : " + "Log=AC cannot be set off.")
                        # return "AC cannot be set off. Error in server."

                if "action_increasetemperature_winter" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_increasetemperature_winter")
                    thvalue = 70.00
                    status = readThermostatStatus(log)
                    if status == "On":
                        try:
                            requests.post("http://localhost:5000/thermostat", json={"temperature": thvalue})
                            log.log_info("Func=" + __name__ + " : " + "Log=Thermostat temperature set to " + str(
                                thvalue) + " degree celsius.")
                            # return "Temperature set to " + str(thvalue) + " degree celsius."
                        except Exception as e:
                            log.log_error("Func=" + __name__ + " : " + "Log=Thermostat temperature cannot be set.")
                            # return "Thermostat temperature cannot be set. Error in server."

            if temperature >= comfort_temperature_winter[1]:
                log.log_info("Func=" + __name__ + " : " + "Log=Temperature is high.")
                if not setThermostatLowGoal(problem_file_path):
                    log.log_error("Func=" + __name__ + " : " + "Log=Error in setting PDDL problem file.")
                else:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Goal set in problem file.")
                solver.solve(log)
                log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

                # Read plan and perform actions
                actions = readActions(log)

                if "action_ac_off" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_ac_off")
                    try:
                        requests.post("http://localhost:5000/ac", json={"status": "Off", "temperature": 0})
                        log.log_info("Func=" + __name__ + " : " + "Log=AC is Off.")
                        # return "Setting AC Off"
                    except Exception as e:
                        log.log_error("Func=" + __name__ + " : " + "Log=AC cannot be set off.")
                        # return "AC cannot be set off. Error in server."

                if "action_decreasetemperature_winter" in actions:
                    log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_decreasetemperature_winter")
                    thvalue = 50.00
                    status = readThermostatStatus(log)
                    if status == "On":
                        try:
                            requests.post("http://localhost:5000/thermostat", json={"temperature": thvalue})
                            log.log_info("Func=" + __name__ + " : " + "Log=Thermostat temperature set to " + str(
                                thvalue) + " degree celsius.")
                            # return "Temperature set to " + str(thvalue) + " degree celsius."
                        except Exception as e:
                            log.log_error("Func=" + __name__ + " : " + "Log=Thermostat temperature cannot be set.")
                            # return "Thermostat temperature cannot be set. Error in server."

        return True

    except Exception as e:
        log.log_error(f"AI Planner has encountered an error!")
        print(e)
        return False


def setLampValue(log, value: float):
    try:
        requests.post("http://localhost:5000/luminance", json={"lamp_lumaval": value})
        log.log_debug("Func=" + __name__ + " : " + "Log=Lamp luminance set to " + str(value))
    except Exception as e:
        log.log_error("Func=" + __name__ + " : " + "Log=Luminance cannot be set")


def readActions(log):
    ac = []
    try:
        with open(plan_file_path, "r") as f:
            action = f.readlines()
            for i in action:
                act = re.search("^([^\w\-]+)*([\w\-]+)", i).group(2)
                ac.append(act)
            return ac
    except Exception as e:
        log.log_debug("Func=" + __name__ + " : " + "Log=Plan doesn't exist.")
        return ac

from AI_Planner.pddl import *
from readSensorValues import *
from setGoal import *
from Sensors.InitializedActuators import lamp
import requests
import time
import re

plan_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\plan.txt")
problem_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\Energy-Optimiser-Problem.pddl")

def OptimiseRoom(log):

    solver = Solver(
        domain_file="Energy-Optimiser-Domain.pddl",
        problem_file="Energy-Optimiser-Problem.pddl",
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

        motion = "notdetected" # Hard coded

        if (season == "Summer") and (motion == "notdetected"):
            log.log_info("Func=" + __name__ + " : " + "Log=Season is summer and motion is not detected in the room")
            if not setSummerOptimiserGoal(problem_file_path):
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

            if "action_lights_off" in actions:
                log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_lights_off")
                try:
                    requests.post("http://localhost:5000/luminance", json={"lamp_lumaval": 0})
                    log.log_info("Func=" + __name__ + " : " + "Log=Lights have been turned off")
                    # return "Lights have been turned off"
                except Exception as e:
                    log.log_error("Func=" + __name__ + " : " + "Log=Lights cannot be turned off")
                    # return "Lights cannot be turned off. Error in server."

        elif (season == "Winter") and (motion == "notdetected"):
            log.log_info("Func=" + __name__ + " : " + "Log=Season is winter and motion is not detected in the room")
            if not setWinterOptimiserGoal(problem_file_path):
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

            if "action_lights_off" in actions:
                log.log_debug("Func=" + __name__ + " : " + "Log=Performing action action_lights_off")
                try:
                    requests.post("http://localhost:5000/luminance", json={"lamp_lumaval": 0})
                    log.log_info("Func=" + __name__ + " : " + "Log=Lights have been turned off")
                    # return "Lights have been turned off"
                except Exception as e:
                    log.log_error("Func=" + __name__ + " : " + "Log=Lights cannot be turned off")
                    # return "Lights cannot be turned off. Error in server."

        else:
            log.log_error("Func=" + __name__ + " : " + "Log=Unable to Optimise Energy")

        return True

    except Exception as e:
        log.log_error(f"AI Planner has encountered an error!")
        print(e)
        return False

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
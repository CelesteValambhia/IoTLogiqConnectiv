from AI_Planner.pddl import *
from readSensorValues import *
from setGoal import *
from Sensors.InitializedActuators import lamp
import requests
import time
import re


comfort_temperature = (20.00, 30.00)
comfort_luminance = (50.00, 70.00)

plan_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\plan.txt")
problem_file_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\Comfort_Analyser_Problem.pddl")

def SetRoomLightComfortable(log):

    solver = Solver(
        domain_file="Comfort_Analyser_Domain.pddl",
        problem_file="Comfort_Analyser_Problem.pddl",
        # problem_template=f"{PDDL_Directory}/problem_template.pddl",
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
        # TODO
        solver.solve(log)
        log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")

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

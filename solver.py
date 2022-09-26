from AI_Planner.logger import *
from AI_Planner.pddl import *

comfort_temperature = (20, 30)
comfort_luminance = (50, 70)

def SetRoomTempComfortable(log):
    solver = Solver(
        domain_file="Comfort_Analyser_Domain.pddl",
        problem_file="Comfort_Analyser_Problem.pddl",
        # problem_template=f"{PDDL_Directory}/problem_template.pddl",
        solution_filename="plan.txt",
        solver_uri="http://solver.planning.domains/solve",
    )
    try:
        solver.solve(log)
        log.log_debug("Func=" + __name__ + " : " + "Log=Plan generated.")
        return True
    except Exception as e:
        log.log_error(f"AI Planner has encountered an error!")
        print(e)
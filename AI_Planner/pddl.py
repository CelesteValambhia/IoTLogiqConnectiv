import requests
import os


class Solver:
    def __init__(self, domain_file: str, problem_file: str,  # problem_template: str,
                 solution_filename: str, solver_uri: str) -> None:
        self.domain_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\")
        self.problem_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\")
        self.solution_path = str(os.getcwd() + "\\AI_Planner\\PDDL_Files\\")
        self.domain_file = f"{str(os.path.join(self.domain_path, domain_file))}"
        self.problem_file = f"{str(os.path.join(self.problem_path, problem_file))}"
        # self.problem_template = problem_template
        self.solution_file = f"{str(os.path.join(self.solution_path, solution_filename))}"
        self.solver_uri = solver_uri

    def solve(self, log):
        body = {
            "domain": open(self.domain_file, "r").read(),
            "problem": open(self.problem_file, "r").read(),
        }
        log.log_info("Func=" + __name__ + " : " + "Log=Sending the request to: " + self.solver_uri)
        response = requests.post(self.solver_uri, json=body).json()
        log.log_info("Func=" + __name__ + " : " + "Log=Received response from: " + self.solver_uri)

        # print(response)
        if response["status"] == "error":
            print(f"{response['result']['output']}")
            log.log_error("Func=" + __name__ + " : " + "Log=AI Planner Compilation Error!")
        elif response["status"] == "ok":
            with open(self.solution_file, "w") as f:
                for act in response["result"]["plan"]:
                    f.write(str(act["name"]))
                    f.write("\n")
        else:
            log.log_error("Func=" + __name__ + " : " + "Log=AI Planner No Response!")

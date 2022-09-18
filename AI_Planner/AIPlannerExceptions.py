from AI_Planner.logger import IoTLogger

log = IoTLogger()

class Error(Exception):
    """
    Parent of AI Planner errors
    """
    log.log_error("Func=" + __name__ + " : " + "Log=AI Planner Error!")


class AIPlanCompilationError(Error):
    """
    Whenever the solver is unable to solve the domain and problem, throws this error !!!
    """

    def __init__(self, response, *args: object) -> None:
        super().__init__(*args)
        log.log_error("Func=" + __name__ + " : " + "Log=AI Planner Compilation Error!")
        print(f"{response['result']['output']}")


class AIPlanCrashError(Error):
    """
    Whenever the AI Planner crashes with miscelleneous reasons, throws this error !!!
    """
    log.log_error("Func=" + __name__ + " : " + "Log=AI Planner Crashed!")


class AIPlanerNoResponseError(Error):
    """
    Whenever the AI Planner doesn't response, throw this error !!!
    """
    log.log_error("Func=" + __name__ + " : " + "Log=AI Planner No Response!")


class ExecutorCannotOpenPlan(Error):
    """
    Whenever the exector cannot open a plan happens.
    """

    def __init__(self, path: str, *args: object) -> None:
        super().__init__(*args)
        self.path = path

    def __str__(self) -> str:
        log.log_error("Func=" + __name__ + " : " + "Log=Cannot open the plan at: " + self.path)
        return f"Cannot open the plan at: {self.path}"


class CompriserOptimum(Error):
    """
    Whenever the compriser realizes the state in no change span, throws this error !!!
    """

    def __str__(self) -> str:
        return "Compriser states : \t The current state is optimum"

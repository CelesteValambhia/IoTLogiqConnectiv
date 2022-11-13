class AC:
    def __init__(self) -> None:
        self.temperature = 25
        self.status = "On"

    def set(self, value: float) -> None:
        if self.status == "On":
            self.temperature = value
            print(f"AC.set : {self.temperature}")
        else:
            print(f"AC cannot be set")

    def get(self) -> float:
        if self.status == "On":
            print(self.temperature)
            return self.temperature
        else:
            return 0

    def setstatus(self, status):
        self.status = status
        print(f"AC.status : {self.status}")

    def getstatus(self) -> str:
        print(self.status)
        return self.status

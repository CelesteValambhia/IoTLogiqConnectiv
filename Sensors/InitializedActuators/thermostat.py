class Thermostat:
    def __init__(self) -> None:
        self.temperature = 0

    def set(self, value: float) -> None:
        self.temperature = value
        print(f"Thermostat.set : {self.temperature}")

    def get(self) -> float:
        print(self.temperature)
        return self.temperature

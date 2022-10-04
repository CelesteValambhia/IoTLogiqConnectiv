class Lamp:
    def __init__(self) -> None:
        self.luma = 0

    def set(self, value: float) -> None:
        self.luma = value
        print(f"lamp.set : {self.luma}")

    def get(self) -> float:
        print(self.luma)
        return self.luma


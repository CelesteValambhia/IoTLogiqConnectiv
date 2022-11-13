from pyowm import OWM
from tqdm import tqdm

OWM_KEY = "b22eb36b4ee111f22c785847a89df5d7"
city: str = "Stuttgart, Germany"

class OWMClient:
    def __init__(self, key: str, city: str = None, location: tuple = None) -> None:
        try:
            print("Connecting to OpenWeatherMap API")
            print("https://www.openweathermap.org/")
            for i in tqdm(range(100)):
                pass
            self.__owm = OWM(key)
            self.mgr = self.__owm.weather_manager()
            print("Connected!")
        except Exception as e:
            print(str(e))
            print("Please check for the API key Validity")

        if city is None and location is None:
            print("No location found")
            print("Please enter a valid city or location")

        else:
            self.__city = city
            self.__location = location
        self.observation = self.get_observation()

    def get_observation(self):
        if not (self.__city is None):
            return self.mgr.weather_at_place(str(self.__city))
        loc_lat, loc_long = self.__location
        return self.mgr.weather_at_coords(loc_lat, loc_long)

    def get_weather(self):
        # return self.__observation.get_weather()
        return self.observation.weather

    def get_status(self) -> str:
        return self.get_weather().status

    def get_temperature(self):
        return self.get_weather().temperature('celsius')['temp']

    def get_wind_status(self):
        return self.get_weather().wind

    def get_humidity(self) -> int:
        return self.get_weather().humidity


if __name__ == "__main__":
    owm_client = OWMClient(key=OWM_KEY, city=city)
    print(owm_client.get_wind_status())

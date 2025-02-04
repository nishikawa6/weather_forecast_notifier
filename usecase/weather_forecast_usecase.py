from abc import ABC, abstractmethod
from usecase.input_data import InputData

class WeatherForecastUseCase(ABC):
    @abstractmethod
    def get_and_notify_weather_forecaset(self, input_data:InputData):
        raise NotImplementedError
from abc import ABC, abstractmethod
from entity.forecast_data import ForecastData
from usecase.input_data import InputData

class iWeatherForecastAdapter(ABC):
    @abstractmethod
    def execute(self, raw_input_data) -> InputData:
        raise NotImplementedError
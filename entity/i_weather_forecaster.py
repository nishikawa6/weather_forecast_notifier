from abc import ABC, abstractmethod


class iWeatherForecaster(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
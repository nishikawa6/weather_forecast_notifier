from abc import ABC, abstractmethod
from entity.forecast_data import ForecastData
from usecase.output_data import OutputData

class iNotificationPresenter(ABC):
    @abstractmethod
    def output(self, forecast_data: OutputData):
        raise NotImplementedError
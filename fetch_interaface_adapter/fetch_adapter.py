from usecase.input_data import InputData
from fetch_interaface_adapter.fetch_data import FetchData
from usecase.forecast_usecase import iForecastUseCase


class FeatchAdapter:
    def __init__(self, forecast_usecase: iForecastUseCase) -> None:
        self.forecaset_usecase = forecast_usecase

    def translate(self, fetched_data: FetchData):
        input_data = InputData(fetched_data.text)
        self.forecaset_usecase.get_and_notify_weather_forecaset(input_data)
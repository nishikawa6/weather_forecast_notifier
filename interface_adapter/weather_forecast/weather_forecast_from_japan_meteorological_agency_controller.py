from usecase.weather_forecast_usecase import WeatherForecastUseCase
from usecase.input_data import InputData
from interface_adapter.weather_forecast.weather_forecast_from_japan_meteorological_agency_data import WeatherForecastFromJapanMeteorologicalAgencyData
from injector import inject

class WeatherForecastFromJapanMeteorologicalAgencyController():
    @inject
    def __init__(self, weahter_forecast_usecase: WeatherForecastUseCase) -> None:
        self.weahter_forecast_usecase = weahter_forecast_usecase

    def execute(self, raw_input_data: WeatherForecastFromJapanMeteorologicalAgencyData):
        input_data = InputData(raw_input_data.json()["text"])
        self.weahter_forecast_usecase.get_and_notify_weather_forecaset(input_data=input_data)

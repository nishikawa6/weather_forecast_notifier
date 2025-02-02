from infrastructure.env import iEnv
from interface_adapter.weather_forecast.weather_forecast_from_japan_meteorological_agency_data import WeatherForecastFromJapanMeteorologicalAgencyData

class WeatherForecastFromJapanMeteorologicalAgency:
    def __init__(self,env:iEnv):
        self.__url = env.WEATHER_FORECAST_API
    
    @property
    def url(self):
        return self.__url

    def execute(self) -> WeatherForecastFromJapanMeteorologicalAgencyData:
        import requests
        # TODO: エラーハンドリングを追加する
        return requests.get(self.__url)


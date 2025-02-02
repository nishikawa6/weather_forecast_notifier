from interface_adapter.weather_forecast.weather_forecast_from_japan_meteorological_agency_data import WeatherForecastFromJapanMeteorologicalAgencyData


class WeatherForecastFromJapanMeteorologicalAgency:
    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv(".env")
        self.__url = os.getenv("WEATHER_FORECAST_API")
    
    @property
    def url(self):
        return self.__url

    def execute(self) -> WeatherForecastFromJapanMeteorologicalAgencyData:
        import requests
        # TODO: エラーハンドリングを追加する
        return requests.get(self.__url)


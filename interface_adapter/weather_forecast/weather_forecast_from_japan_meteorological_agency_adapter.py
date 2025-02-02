from usecase.i_weather_forecast_adapter import iWeatherForecastAdapter
from usecase.input_data import InputData
from interface_adapter.weather_forecast.weather_forecast_from_japan_meteorological_agency_data import WeatherForecastFromJapanMeteorologicalAgencyData


class WeatherForecastFromJapanMeteorologicalAgencyAdapter(iWeatherForecastAdapter):
    def execute(self, raw_input_data: WeatherForecastFromJapanMeteorologicalAgencyData) -> InputData:
        return InputData(raw_input_data.json()["text"])
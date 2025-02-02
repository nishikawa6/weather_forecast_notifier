from entity import *
from usecase import *
from interface_adapter import *
from infrastructure import *
from injector import Injector

class Dependency:
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)
    
    @classmethod
    def config(cls, binder):
        binder.bind(iNotifier, LineNotify)
        binder.bind(iWeatherForecaster, WeatherForecastFromJapanMeteorologicalAgency)
       
        binder.bind(iNotificationAdapter, LineNotifyAdapter)
        binder.bind(iWeatherForecastAdapter, WeatherForecastFromJapanMeteorologicalAgencyAdapter)

    def resolve(self, cls):
        return self.injector.get(cls)

def main():
    injector = Dependency()
    weather_forecast_usecase = injector.resolve(WeatherForecastUseCase)

    weather_forecast_usecase.get_and_notify_weather_forecaset()


if __name__ == "__main__":
    main()
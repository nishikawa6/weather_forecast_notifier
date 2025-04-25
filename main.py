from entity import *
from usecase import *
from interface_adapter import *
from infrastructure import *
from injector import Injector

class UsecaseDependency:
    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)
    
    @classmethod
    def config(cls, binder):
        binder.bind(WeatherForecastUseCase, WeatherForecastInteractor)
        binder.bind(iNotificationPresenter, LineNotifyPresenter)

    def resolve(self, cls):
        return self.injector.get(cls)



def main():
    injector = UsecaseDependency()
    weather_forecast_api = WeatherForecastFromJapanMeteorologicalAgency()
    weather_forecast_controller = injector.resolve(WeatherForecastFromJapanMeteorologicalAgencyController)
    line_notify = LineNotify()

    weather_forecast_controller.execute(weather_forecast_api.execute())
    line_notify.execute()


if __name__ == "__main__":
    main()
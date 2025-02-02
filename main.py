from entity import *
from usecase import *
from interface_adapter import *
from infrastructure import *

def main():
    env = Env()
    weather_forecaster = WeatherForecastFromJapanMeteorologicalAgency(env)
    notifier = LineNotify(env)
    weather_forecast_adapter = WeatherForecastFromJapanMeteorologicalAgencyAdapter()
    notification_adapter = LineNotifyAdapter()
    weather_forecast_usecase = WeatherForecastUseCase(
        notifier=notifier,
        weather_forecaster= weather_forecaster,
        notification_adapter=notification_adapter,
        weather_forecast_adapter=weather_forecast_adapter
    )

    weather_forecast_usecase.get_and_notify_weather_forecaset()


if __name__ == "__main__":
    main()
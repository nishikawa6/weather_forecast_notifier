from entity.i_notifier import iNotifier
from entity.i_weather_forecaster import iWeatherForecaster
from entity.forecast_data import ForecastData
from usecase.i_notification_adapter import iNotificationAdapter
from usecase.i_weather_forecast_adapter import iWeatherForecastAdapter
from usecase.input_data import InputData
from usecase.output_data import OutputData
from injector import inject


class WeatherForecastUseCase():
    @inject
    def __init__(
        self, 
        notifier: iNotifier,
        weather_forecaster: iWeatherForecaster,
        notification_adapter: iNotificationAdapter,
        weather_forecast_adapter: iWeatherForecastAdapter,
        ) -> None:
        self.notifier = notifier
        self.weather_forecaster = weather_forecaster
        self.notification_adapter = notification_adapter
        self.weather_forecast_adapter = weather_forecast_adapter

    def get_and_notify_weather_forecaset(self) -> None:
        # 外部APIから取得したデータをuse caseが扱いやすいように変換して取得する
        # また、Interface AdapterとUse caseの境界を超えるための処理でもある
        input_data: InputData = self.weather_forecast_adapter.execute(self.weather_forecaster.execute())
        
        # entityが扱いやすいようにデータを変換する（use caseの役割の一つ）
        forecast_data = self.input_data2forecast_data(input_data)

        # entityで扱うデータ形式をuse caseで扱いやすい形式に変換する
        output_data: OutputData = self.forecast_data2output_data(forecast_data)

        # use caseで扱いやすいデータ形式から外部APIが扱いやすいデータ形式に変換する
        # また、Interface AdapterとUse caseの境界を超えるための処理でもある
        self.notifier.execute(self.notification_adapter.execute(output_data))
    
    def input_data2forecast_data(self, input_data:InputData) -> ForecastData:
        return ForecastData(input_data.text)
    
    def forecast_data2output_data(self, forecast_data: ForecastData) -> OutputData:
        return OutputData(forecast_data.forcast_message)

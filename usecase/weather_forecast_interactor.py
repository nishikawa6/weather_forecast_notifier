from entity.forecast_data import ForecastData
from usecase.i_notification_presenter import iNotificationPresenter
from usecase.input_data import InputData
from usecase.output_data import OutputData
from usecase.weather_forecast_usecase import WeatherForecastUseCase
from injector import inject


class WeatherForecastInteractor(WeatherForecastUseCase):
    @inject
    def __init__(
        self, 
        notification_presenter: iNotificationPresenter,
        ) -> None:
        self.notification_presenter = notification_presenter

    def get_and_notify_weather_forecaset(self, input_data:InputData):
        # entityが扱いやすいようにデータを変換する（use caseの役割の一つ）
        forecast_data: ForecastData = self.input_data2forecast_data(input_data)

        # entityで扱うデータ形式をuse caseで扱いやすい形式に変換する
        output_data: OutputData = self.forecast_data2output_data(forecast_data)

        # use caseで扱いやすいデータ形式から外部APIが扱いやすいデータ形式に変換する
        # また、Interface AdapterとUse caseの境界を超えるための処理でもある
        self.notification_presenter.output(output_data)
    
    def input_data2forecast_data(self, input_data:InputData) -> ForecastData:
        return ForecastData(input_data.text)
    
    def forecast_data2output_data(self, forecast_data: ForecastData) -> OutputData:
        return OutputData(forecast_data.forcast_message)

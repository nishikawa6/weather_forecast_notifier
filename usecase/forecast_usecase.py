from abc import ABC, abstractmethod
from i_notification_adapter import iNotificationAdapter


class iForecastUseCase(ABC):
    @abstractmethod
    def get_and_notify_weather_forecaset(self, input_data):
        raise NotImplementedError


class ForecastUseCase(iForecastUseCase):
    def __init__(self, notification_adapter: iNotificationAdapter) -> None:
        self.notification_adapter = notification_adapter

    def notify_weather_forecaset(self, input_data):
        self.notification_adapter.translate(input_data)

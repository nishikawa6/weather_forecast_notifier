from usecase.i_notification_adapter import iNotificationAdapter
from usecase.output_data import OutputData
from notification_interface_adapter.notification_data import NotificationData


class NotificationAdapter(iNotificationAdapter):
    def translate(self, data:OutputData):
        notification_data = NotificationData(data.message)
        return notification_data
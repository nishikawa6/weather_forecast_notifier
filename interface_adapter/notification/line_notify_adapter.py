from usecase.i_notification_adapter import iNotificationAdapter
from usecase.output_data import OutputData
from interface_adapter.notification.line_notify_data import LineNotifyData


class LineNotifyAdapter(iNotificationAdapter):
    def execute(self, output_data:OutputData) -> LineNotifyData:
        notification_data = LineNotifyData(output_data.message)
        return notification_data
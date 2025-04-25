from usecase.i_notification_presenter import iNotificationPresenter
from usecase.output_data import OutputData
from interface_adapter.notification.line_notify_view_model import LineNotifyData


class LineNotifyPresenter(iNotificationPresenter):
    def output(self, output_data:OutputData) -> LineNotifyData:
        LineNotifyData(output_data.message)
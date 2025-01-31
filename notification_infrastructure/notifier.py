from notification_interface_adapter.notification_data import NotificationData

class Notifier:
    def notify(self,notification_data: NotificationData):
        print('通知を送信：',notification_data)
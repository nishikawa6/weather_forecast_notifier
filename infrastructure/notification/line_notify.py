from interface_adapter.notification.line_notify_view_model import LineNotifyData


class LineNotify:
    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv(".env")
        self.__line_notify_api = os.getenv("LINE_NOTIFY_API")
        self.__line_notify_token = os.getenv("LINE_NOTIFY_TOKEN")

    def execute(self):
        import requests

        notification_message = LineNotifyData()
        headers = {'Authorization': f'Bearer {self.__line_notify_token}'}
        data = {'message': f'{notification_message.notification_message}'}
        requests.post(self.__line_notify_api, headers = headers, data = data)
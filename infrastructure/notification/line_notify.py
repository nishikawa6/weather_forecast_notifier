from infrastructure.env import iEnv
from interface_adapter.notification.line_notify_data import LineNotifyData

class LineNotify:
    def __init__(self, env: iEnv):
        self.__line_notify_api = env.LINE_NOTIFY_API
        self.__line_notify_token = env.LINE_NOTIFY_TOKEN

    def execute(self, notification_message: LineNotifyData):
        import requests

        headers = {'Authorization': f'Bearer {self.__line_notify_token}'}
        data = {'message': f'{notification_message.notification_message}'}
        requests.post(self.__line_notify_api, headers = headers, data = data)
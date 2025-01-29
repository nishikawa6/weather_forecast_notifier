from env import iEnv
from abc import ABC, abstractclassmethod

class iNotifier(ABC):
    @abstractclassmethod
    def send(self):
        pass

class LineNotify(iNotifier):
    def __init__(self, env: iEnv, message):
        self.__line_notify_api = env.LINE_NOTIFY_API
        self.__line_notify_token = env.LINE_NOTIFY_TOKEN
        self.__message = message

    def send(self):
        import requests

        headers = {'Authorization': f'Bearer {self.__line_notify_token}'}
        data = {'message': f'{self.__message}'}
        requests.post(self.__line_notify_api, headers = headers, data = data)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, msg):
        self.__message = msg

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv('.env.develop')
    line_notify = LineNotify(
        line_notify_api=os.getenv('LINE_NOTIFY_API'),
        line_notify_token=os.getenv('LINE_NOTIFY_TOKEN'),
        message='Hello World!'
    )

    line_notify.send()
    line_notify.message = 'changed message'
    line_notify.send()
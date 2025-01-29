
class NotificationMessage:
    def __init__(self, row_message):
        self.__row_message = row_message.json()
    
    def message(self):
        return self.__row_message['text']


if __name__=='__main__':
    import requests
    import os
    from dotenv import load_dotenv

    print(os.getcwd())
    load_dotenv('.env.develop')
    url = os.getenv('WEATHER_FORECAST_API')

    response = requests.get(url)

    notify_message = NotificationMessage(row_message=response)
    print(notify_message.message())

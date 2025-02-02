from abc import ABC, abstractmethod

class iEnv(ABC):
    @abstractmethod
    def LINE_NOTIFY_TOKEN(self):
        pass

    @abstractmethod
    def LINE_NOTIFY_API(self):
        pass

    @abstractmethod
    def WEATHER_FORECAST_API(self):
        pass

# REVIEW: dataclassを用いた方が適切かもしれない
class Env(iEnv):
    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv('.env')
        self.__LINE_NOTIFY_TOKEN=os.getenv('LINE_NOTIFY_TOKEN')
        self.__LINE_NOTIFY_API=os.getenv('LINE_NOTIFY_API')
        self.__WEATHER_FORECAST_API=os.getenv('WEATHER_FORECAST_API')

    @property
    def LINE_NOTIFY_TOKEN(self):
        return self.__LINE_NOTIFY_TOKEN

    @property
    def LINE_NOTIFY_API(self):
        return self.__LINE_NOTIFY_API
    
    @property
    def WEATHER_FORECAST_API(self):
        return self.__WEATHER_FORECAST_API


if __name__ == '__main__':
    env = Env()

    print(env.LINE_NOTIFY_API)
    print(env.LINE_NOTIFY_TOKEN)
    print(env.WEATHER_FORECAST_API)
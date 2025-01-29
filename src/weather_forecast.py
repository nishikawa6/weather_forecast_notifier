from env import iEnv
from abc import ABC,abstractclassmethod

class iForecaster(ABC):
    @property
    @abstractclassmethod
    def url(self):
        pass

    @abstractclassmethod
    def get(self):
        pass

class WeatherForecast(iForecaster):
    def __init__(self,env:iEnv):
        self.__url = env.WEATHER_FORECAST_API
    
    @property
    def url(self):
        return self.__url

    def get(self):
        import requests
        # TODO: エラーハンドリングを追加する
        return requests.get(self.__url)
    
        

if __name__=='__main__':
    import requests
    from env import Env

    env = Env()

    weather_forecast = WeatherForecast(env)
    print(weather_forecast.get())

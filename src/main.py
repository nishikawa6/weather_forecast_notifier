from env import Env
from weather_forecast import WeatherForecast
from line_notify import LineNotify
from notification_message import NotificationMessage

def main():
    env = Env()
    forecaster = WeatherForecast(env)

    # 天気予報情報を取得
    response = forecaster.get() 

    # 通知メッセージを作成
    messager = NotificationMessage(response)
    message = messager.message()
    
    # メッセージを送信
    notifier = LineNotify(env, message)
    notifier.send()
    

if __name__=='__main__':
    main()
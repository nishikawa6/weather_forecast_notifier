from dataclasses import dataclass

@dataclass
class ForecastData:
    '''
    天気予報の情報を表すエンティティ
    '''
    forcast_message: str
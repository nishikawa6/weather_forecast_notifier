from dataclasses import dataclass

@dataclass
class WeatherForecastFromJapanMeteorologicalAgencyData:
    publishingOffice: str
    reportDatetime: str
    targetArea: str
    headlineText: str
    text: str
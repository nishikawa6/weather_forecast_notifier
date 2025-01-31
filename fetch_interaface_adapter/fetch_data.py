from dataclasses import dataclass

@dataclass
class FetchData:
    publishingOffice: str
    reportDatetime: str
    targetArea: str
    headlineText: str
    text: str
from abc import ABC, abstractmethod
from usecase.output_data import OutputData

class iNotificationAdapter(ABC):
    @abstractmethod
    def translate(self, data: OutputData):
        raise NotImplementedError
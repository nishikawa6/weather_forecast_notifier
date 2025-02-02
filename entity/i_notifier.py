from abc import ABC, abstractmethod


class iNotifier(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
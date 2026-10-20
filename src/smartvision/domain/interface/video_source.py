from abc import ABC, abstractmethod

class VideoSource(ABC):
    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError("Subclasses must implement the connect method.")
    pass

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError("Subclasses must implement the disconnect method.")
    pass

    @abstractmethod
    def read_frame(self) -> None:
        raise NotImplementedError("Subclasses must implement the read_frame method.")
    pass
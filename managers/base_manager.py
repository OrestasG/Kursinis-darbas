from abc import ABC, abstractmethod


class BaseManager(ABC):
    """Abstract base class for managers."""

    @abstractmethod
    def add_item(self):
        pass

    @abstractmethod
    def list_items(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass
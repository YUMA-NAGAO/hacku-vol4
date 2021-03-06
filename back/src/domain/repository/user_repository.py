from abc import ABCMeta, abstractmethod

from src.domain.entity import UserEntity


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self, new_user: UserEntity):
        pass

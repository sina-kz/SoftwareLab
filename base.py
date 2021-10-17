from abc import ABC

from manager import Manager


class BaseClass(ABC):
    _id = 0
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)


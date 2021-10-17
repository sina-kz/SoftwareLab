from base import BaseClass


class Region(BaseClass):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"name: {self.name}"

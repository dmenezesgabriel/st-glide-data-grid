from abc import ABC


class BaseColumn(ABC):
    def __init__(self, title, width=100, kind="Text"):
        self.title = title
        self.width = width
        self.kind = kind

    def to_dict(self):
        return {
            "title": self.title,
            "width": self.width,
            "kind": self.kind,
        }


class TextColumn(BaseColumn):
    def __init__(self, title, width=100):
        super().__init__(title, width, kind="Text")


class NumberColumn(BaseColumn):
    def __init__(self, title, width=100, precision=2):
        super().__init__(title, width, kind="Number")
        self.precision = precision

    def to_dict(self):
        base_dict = super().to_dict()
        return base_dict

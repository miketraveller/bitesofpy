from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self):
        self._x = None

    @property
    def expired(self):
        return self._x
        
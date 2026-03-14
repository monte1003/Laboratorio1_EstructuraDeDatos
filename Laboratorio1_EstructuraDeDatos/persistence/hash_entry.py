"""Entidad base para una entrada de tabla hash."""


class HashEntry:
    def __init__(self, key, value_reference):
        self.key = key
        self.value_reference = value_reference

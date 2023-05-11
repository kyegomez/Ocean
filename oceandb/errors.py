from abc import abstractmethod


class OceanError(Exception):
    def code(self):
        """Return an appropriate HTTP response code for this error"""
        return 400  # Bad Request

    def message(self):
        return ", ".join(self.args)

    @classmethod
    @abstractmethod
    def name(self):
        """Return the error name"""
        pass


class NoDatapointsException(OceanError):
    @classmethod
    def name(cls):
        return "NoDatapoints"


class NoIndexException(OceanError):
    @classmethod
    def name(cls):
        return "NoIndex"


class InvalidDimensionException(OceanError):
    @classmethod
    def name(cls):
        return "InvalidDimension"


class NotEnoughElementsException(OceanError):
    @classmethod
    def name(cls):
        return "NotEnoughElements"


class IDAlreadyExistsError(OceanError):
    def code(self):
        return 409  # Conflict

    @classmethod
    def name(cls):
        return "IDAlreadyExists"


class DuplicateIDError(OceanError):
    @classmethod
    def name(cls):
        return "DuplicateID"


class InvalidUUIDError(OceanError):
    @classmethod
    def name(cls):
        return "InvalidUUID"


error_types = {
    "NoDatapoints": NoDatapointsException,
    "NoIndex": NoIndexException,
    "InvalidDimension": InvalidDimensionException,
    "NotEnoughElements": NotEnoughElementsException,
    "IDAlreadyExists": IDAlreadyExistsError,
    "DuplicateID": DuplicateIDError,
    "InvalidUUID": InvalidUUIDError,
}

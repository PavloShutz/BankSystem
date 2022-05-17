"""Specific exceptions for Bank System"""


class InvalidPinError(Exception):
    """Raises an exception, if pin is invalid."""

    def __init__(self, user_pin,
                 message="expected valid input( pin is int, len(pin) = 4 )"):
        self.user_pin = user_pin
        self.message = message

    def __str__(self):
        return f"{self.message}, instead got: {self.user_pin}"

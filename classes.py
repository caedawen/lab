class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self, channel: int, volume: int, status: bool) -> None:
        """
        Constructor to create initial state of a television object.
        :param channel: Television's initial channel setting.
        :param volume: Television's initial volume setting.
        :param status: Television's initial status setting.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self, status: bool) -> None:
        """
        Method to turn the TV on/off.
        If called on a TV object that is off, the TV object should be turned on.
        If called on a TV object that is on, the TV object should be turned off.
        """
        self.__status = not self.__status


    def channel_up(self, channel: int) -> None:
        """
        Method to adjust the TV channel by incrementing its value if the television is on.
        If the television is on the MAX_CHANNEL, it is set to MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1


    def channel_down(self, channel: int) -> None:
        """
        Method to adjust the TV channel by decrementing its value if the television is on.
        If the television is on MIN_CHANNEL, it is set to MAX_CHANNEL.

        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self, volume: int) -> None:
        """
        Method to adjust the TV volume by incrementing its value if the television is on.
        If the television is already at MAX_VOLUME, the volume remains the same.
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self, volume: int) -> None:
        """
        Method to adjust the TV volume by decrementing its value if the television is on.
        If the television is already at MIN_VOLUME, the volume remains the same.
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return TV params in an easy to read format.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


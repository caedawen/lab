class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Method to turn the TV on/off.
        """
        self.__status = not self.__status


    def channel_up(self) -> None:
        """
        Method to adjust the TV channel by incrementing its value if the television is on.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1


    def channel_down(self) -> None:
        """
        Method to adjust the TV channel by decrementing its value if the television is on.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to adjust the TV volume by incrementing its value if the television is on.
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1


    def volume_down(self) -> None:
        """
        Method to adjust the TV volume by decrementing its value if the television is on.
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


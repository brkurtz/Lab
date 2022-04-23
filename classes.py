class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial Tv settings. Channel = 0, Volume = 0, Status = False
        """
        self.__chan = 0
        self.__vol = 0
        self.__status = False
        pass

    def power(self) -> None:
        """
        Method to turn Tv on or off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
        pass

    def channel_up(self) -> None:
        """
        Method to raise Tv channel by 1. Will only work if Tv is on. If channel goes above MAX_CHANNEL it will go to
        MIN_CHANNEL.
        """
        if self.__status:
            self.__chan += 1
            if self.__chan > self.MAX_CHANNEL:
                self.__chan = self.MIN_CHANNEL

        pass

    def channel_down(self) -> None:
        """
        Method to lower Tv channel by 1. Will only work if Tv is on. If channel goes below MIN_CHANNEL it will go to
        MAX_CHANNEL.
        """
        if self.__status:
            self.__chan -= 1
            if self.__chan < self.MIN_CHANNEL:
                self.__chan = self.MAX_CHANNEL
        pass

    def volume_up(self) -> None:
        """
        Method to raise Tv volume by 1. Will only work if Tv is on. If volume is at MAX_VOLUME it will not be adjusted
        """
        if self.__status:
            if self.__vol != self.MAX_VOLUME:
                self.__vol += 1
        pass

    def volume_down(self) -> None:
        """
        Method to lower Tv volume by 1. Will only work if Tv is on. If volume is at MIN_VOLUME it will not be adjusted
        """
        if self.__status:
            if self.__vol != self.MIN_VOLUME:
                self.__vol -= 1
        pass

    def __str__(self) -> str:
        """
        Method to print Tv status

        :return: TV status using the format shown in the comments of main.py
        """
        return f'TV status: Is on = {self.__status}. Channel = {self.__chan}, Volume = {self.__vol}'
        pass

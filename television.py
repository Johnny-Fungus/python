class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method that initializes the instance variables.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__volume_save = self.__volume

    def power(self) -> None:
        """
        Method that changes the status of the tv to True.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method that mutes and unmutes the tv.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method that increases the channel.
        """
        if self.__status:
            if self.__channel >= self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method that decreases the channel.
        """
        if self.__status:
            if self.__channel <= self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method that increases the volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME and self.__status:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method that decreases the volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME and self.__status:
                self.__volume -= 1


    def __str__(self) -> str:
        """
        Method to show the tv status
        :return: tv status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


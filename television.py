class Television:
    """
    Television class

    Contains 4 class variables and 8 functions with 5 different variables:
        Class variables - define bounds for the volume and channel instance variables
        __status - power state of the TV
        __muted - mute state of the TV (sets volume to zero, maintains previous
                    volume for un-mute
        __volume - current volume integer of TV
        __channel - current channel the TV is set to
        __volumeBeforeMute - variable for maintaining volume before mute

        power(), mute(), channel_up(), channel_down(), volume_up(), volume_down()
            affect their respective variables

        __str()__ returns output for the TV's general status
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes 5 instance variables for each instance of Television
        Defaults for __volume and __channel are set to the minimum for both
        TV power and mute status default to False
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__volumeBeforeMute = 0

    def power(self) -> None:
        """
        Changes power status of instance to the opposite of what it was
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        This function flips the mute state as well as:
            - returning the volume to what it was before muting
        OR
            - saving the volume value to a separate variable, then setting vol to 0
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__volumeBeforeMute
                self.__muted = False
            else:
                self.__volumeBeforeMute = self.__volume
                self.__volume = 0
                self.__muted = True
        else:
            pass

    def channel_up(self) -> None:
        """
        This function will check if the TV is on, increase the channel by 1, as well as check
            whether the channel has surpassed its maximum value.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
        else:
            pass

    def channel_down(self) -> None:
        """
        This function will check if the TV is on, decrease the channel by 1, as well as check
            whether the channel has surpassed its minimum value.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
        else:
            pass
        
    def volume_up(self) -> None:
        """
        This function will check if the TV is on, unmute if the TV is muted, then increase the
            volume by 1 unless it has reached the maximum allowed volume.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
        else:
            pass

    def volume_down(self) -> None:
        """
        This function will check if the TV is on, unmute if the TV is muted, then decrease the
            volume by 1 unless it has reached the minimum allowed volume.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
        else:
            pass

    def __str__(self) -> str:
        """
        This function will return a string giving a general status of the TV.
        Format: 'Power = [state], Channel = [channel #], Volume = [volume #]'
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

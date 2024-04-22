import pytest
from television import Television


def test_television():

    # begin init testing

    # test initial status
    tv_1 = Television()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

    # test power on
    tv_1.power()
    assert tv_1.__str__() == "Power = True, Channel = 0, Volume = 0"

    # test power off
    tv_1.power()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 0"

    # begin mute testing

    # test mute status: power on, vol up, mute
    tv_1.power()
    tv_1.volume_up()
    tv_1.mute()
    assert tv_1.__str__() == "Power = True, Channel = 0, Volume = 0"

    # test mute status: power on, unmute
    tv_1.mute()
    assert tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"

    # test mute status: power off, mute
    tv_1.power()
    tv_1.mute()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 1"

    # test mute status: power off, unmute
    tv_1.mute()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 1"

    # begin channel_up testing

    # test channel_up: power off (state set after last test), inc channel
    tv_1.channel_up()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 1"

    # test channel_up: power on, inc channel
    tv_1.power()
    tv_1.channel_up()
    assert tv_1.__str__() == "Power = True, Channel = 1, Volume = 1"

    # test channel_up: power on, go past max channel
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    assert tv_1.__str__() == "Power = True, Channel = 0, Volume = 1"

    # begin channel_down testing

    # test channel_down: power off, dec channel
    tv_1.power()
    tv_1.channel_down()
    assert tv_1.__str__() == "Power = False, Channel = 0, Volume = 1"

    # test channel_down: power on, dec channel past min
    tv_1.power()
    tv_1.channel_down()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 1"

    # begin volume_up testing

    # test volume_up: power off, volume inc
    tv_1.power()
    tv_1.volume_up()
    assert tv_1.__str__() == "Power = False, Channel = 3, Volume = 1"

    # test volume_up: power on, volume inc
    tv_1.power()
    tv_1.volume_up()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 2"

    # test volume_up: power on, mute, volume inc
    tv_1.mute()
    tv_1.volume_up()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 2"

    # test volume_up: power on, mute, volume inc past max
    tv_1.mute()
    tv_1.volume_up()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 2"

    # begin volume_down testing

    # test volume_down: power off, volume dec
    tv_1.power()
    tv_1.volume_down()
    assert tv_1.__str__() == "Power = False, Channel = 3, Volume = 2"

    # test volume_down: power on, volume dec
    tv_1.power()
    tv_1.volume_down()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 1"

    # test volume_down: power on, mute, volume dec
    tv_1.mute()
    tv_1.volume_down()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 0"

    # test volume_down: power on, volume dec past min
    tv_1.volume_down()
    assert tv_1.__str__() == "Power = True, Channel = 3, Volume = 0"

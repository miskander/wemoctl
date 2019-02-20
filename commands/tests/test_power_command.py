import pytest

from mock import Mock, patch

from commands import NoSuchDeviceError, PowerCommand


@patch('commands.get_device')
def test_raises_NoSuchDevice_when_no_devices(get_device_mock):

    power_cmd = PowerCommand('Test Device', 'on')
    get_device_mock.return_value = []

    with pytest.raises(NoSuchDeviceError):
        power_cmd.execute()


@patch('commands.get_device')
def test_calls_on_when_device_is_found(get_device_mock):

    power_cmd = PowerCommand('Test Device', 'on')
    device_mock = Mock(name='Test Device')
    device_on_method = Mock()

    get_device_mock.return_value = device_mock
    device_mock.on = device_on_method

    power_cmd.execute()

    device_on_method.assert_called_once()


@patch('commands.get_device')
def test_calls_off_when_device_is_found(get_device_mock):
    power_cmd = PowerCommand('Test Device', 'off')
    device_mock = Mock(name='Test Device')
    device_off_method = Mock()

    get_device_mock.return_value = device_mock
    device_mock.off = device_off_method

    power_cmd.execute()

    device_off_method.assert_called_once()
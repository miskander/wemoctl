import pytest

from mock import Mock, patch

from commands import get_device


@patch('commands.pywemo.discover_devices')
def test_get_device_returns_None_if_None_returned(discover_devices_call):
    discover_devices_call.return_value = None

    assert get_device('Test Device') is None


@patch('commands.pywemo.discover_devices')
def test_get_device_returns_None_if_empty_list_returned(discover_devices_call):
    discover_devices_call.return_value = []

    assert get_device('Test Device') is None

@patch('commands.pywemo.discover_devices')
def test_device_is_found_with_mismatched_case(discover_devices_call):
    found_device_mock = Mock()
    found_device_mock.configure_mock(name='test device')
    discover_devices_call.return_value = [found_device_mock]

    found_device = get_device('Test Device')

    assert found_device == found_device_mock
import pywemo
import time


class NoSuchDeviceError(Exception):
    pass


def get_device(device_name):
    device = None

    for attempt in range(3):
        devices = pywemo.discover_devices()

        for d in devices:
            if d.name.lower() == device_name.lower():
                device = d
                break

        if device:
            break
        else:
            print("Attempt #%i to find '%s' failed; will try again..." % (attempt, device_name))
            time.sleep(1)

    return device


class PowerCommand(object):
    def __init__(self, device_name, desired_state):
        self.device_name = device_name
        self.state = desired_state

    def execute(self):
        device = get_device(self.device_name)

        if not device:
            raise NoSuchDeviceError('No such device: ' + self.device_name)

        if self.state == 'on':
            device.on()

        if self.state == 'off':
            device.off()

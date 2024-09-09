from abc import ABC, abstractmethod

class SmartDevice(ABC):
    _name = 'nil'
    _status = None
    def __init__(self, name, status):
        self._name = name
        self._status = status
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self, name, status):
        super().__init__(name, status)
    def turn_on(self):
        print('Light is on')
        self._status = True
    def turn_off(self):
        print('Light is off')
        self._status = False

    def device_info(self):
        print(f"The name of the light is {self._name}")
        if self._status:
            print(f"The status of the light is ON")
        else:
            print(f"The status of the light is OFF")

    def set_brightness(self, brightness):
        print(f'Brightness is set to: {brightness}%')


alexa = SmartLight('alexa', 0)
siri = SmartLight('siri', 0)

siri.set_brightness(7)
siri.turn_on()
siri.device_info()
siri.turn_off()
siri.device_info()
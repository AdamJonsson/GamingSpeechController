import pyaudio

class _Microphone:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    _currentChosenChannel = 1

    def listMicrophoneChannels(self):
        pyaudio_object = pyaudio.PyAudio()
        info = pyaudio_object.get_host_api_info_by_index(0)
        number_of_devices = info.get('deviceCount')
        for i in range(0, number_of_devices):
            device = pyaudio_object.get_device_info_by_host_api_device_index(0, i)
            if (device.get('maxInputChannels')) > 0:
                print (i, "-",  device.get("name"))

    def askUserForInputDevice(self):
        self.listMicrophoneChannels()
        newInputDeviceChannel = int(input("Choose a input device: "))
        self.changeInputDevice(newInputDeviceChannel)

    def changeInputDevice(self, new_channel):
        self._currentChosenChannel = new_channel

    def getMicrophoneStream(self):
        pyaudio_object = pyaudio.PyAudio()
        stream = pyaudio_object.open(format=self.FORMAT,
                        channels=self._currentChosenChannel,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        return stream;

microphone = _Microphone()
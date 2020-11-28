import pyaudio

class _Microphone:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    _current_chosen_channel = 1

    def list_microphone_channels(self):
        pyaudio_object = pyaudio.PyAudio()
        info = pyaudio_object.get_host_api_info_by_index(0)
        number_of_devices = info.get('deviceCount')
        for i in range(0, number_of_devices):
            device = pyaudio_object.get_device_info_by_host_api_device_index(0, i)
            if (device.get('maxInputChannels')) > 0:
                print (i, "-",  device.get("name"))

    def ask_user_for_input_device(self):
        self.list_microphone_channels()
        new_input_device_channel = int(input("Choose a input device: "))
        self.change_input_device(new_input_device_channel)

    def change_input_device(self, new_channel):
        self._current_chosen_channel = new_channel

    def get_microphone_stream(self):
        pyaudio_object = pyaudio.PyAudio()
        stream = pyaudio_object.open(format=self.FORMAT,
                        channels=self._current_chosen_channel,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        return stream;

microphone = _Microphone()
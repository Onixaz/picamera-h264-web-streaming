# Picamera h264 Web Streaming
Demo of h264 live streaming from Raspberry Pi using PiCamera and broadway.js.

## Usage

1.Clone this repository

```
git clone https://github.com/Onixaz/picamera-h264-web-streaming.git
cd picamera-h264-web-streaming
```

2. Create Python3 virtual enviroment (optional)

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install picamera, ws4py
```

4. Launch the server

```
python server.py
```
5. Navigate to http://your-raspberrypi-ip:8082 on your PC and the stream should appear. 

## Credits

https://github.com/waveform80/pistreaming
https://github.com/mbebenita/Broadway




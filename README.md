# qdotweb_rpi

A flask wrapper for gathering data from devices/sensors connected to a Raspberry Pi over a network.

Setup:

- Install package on raspberry pi (still need to make package)
- Install device on raspberry pi
- Edit device.py and add method to get data from device

Use:

- Run qdotweb_rpi from raspberry pi
- From user machine, import requests
- To view available devices: http://localhost:5000
- To request data:

    r = requests.post('http://localhost:5000/read', data={'device':'DEVICE_NAME', 'command':'PARAM_SENT_TO_READ_FUNCTION'})
    jr = r.json()
    print(jr)

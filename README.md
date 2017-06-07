# qdotweb_rpi

A flask wrapper for gathering data from devices/sensors connected to a Raspberry Pi over a network. An example is already installed for reading from a pressure or temperature sensor (connected to Pi) over a network.

Setup:

- Install package on raspberry pi (still need to make package)
- Install device on raspberry pi
- Edit device.py and add method to get data from device

Use:

- Run qdotweb_rpi from raspberry pi
- From user machine, import requests in pyhton script
- To view available devices: http://localhost:5000
- To request data:

    - r = requests.post('http://localhost:5000/read', data={'device':'DEVICE_NAME', 'command':'PARAM_SENT_TO_READ_FUNCTION'})
        - Replace local host with the the address of the rpi on the network. 

    - jr = r.json()

    - print(jr)

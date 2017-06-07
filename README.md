# qdotweb_rpi

A flask wrapper for gathering data from devices/sensors connected to a server over a network. Here is an example for reading a pressure or temperature sensor (connected to a Raspberry Pi) over the lab network.

Setup:

- Install device(s) on raspberry pi
- Edit device.py and add methods(s) to get data from installed device(s)

Use:

- Import Requests
- r = requests.post('http://localhost:5000/read', data={'device':'DEVICE_NAME', 'command':'PARAM_SENT_TO_READ_FUNCTION'})
        - Replace local host with the the address of the rpi on the network. 
- jr = r.json()
- print(jr)

TODO:

- Add a devices request to return a list of devices setup on the server
- Add a secure Login form for the web application


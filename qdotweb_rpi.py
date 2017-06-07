from flask import Flask, render_template, request
from datetime import datetime
import device
from device import Device
import socket
import json
from collections import OrderedDict

if socket.gethostname().find('.')>=0:
    hostname=socket.gethostname()
else:
    hostname=socket.gethostbyaddr(socket.gethostname())[0]
hostname = hostname.split('.')[0]

app = Flask(__name__)

devices = []

def format_devices_table(devlist):
    """ put instruments list into HTML table """
    table = '<table border="1" cellpadding="5" cellspacing="5">'
    table += '<caption>List of available resources:</caption>'
    table += '<tr> <th>Device(s)</th> </tr>'
    for i in devlist:
        table += '<tr> <td>{}</td> </tr>'.format(i)
    table += '</table>'
    return table

@app.route('/')
def index():
    resource_table = format_devices_table(device.DEVICE_NAMES)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', resource_table = resource_table, hostname = hostname, current_time = current_time)

@app.route("/read", methods=['POST', 'GET'])
def query():
    data = ''
    errors = ''
    device = ''
    command = ''
    try:
        if request.method == 'POST':
            post = request.form
            if post['device']:
                device = post['device']
            else:
                raise ValueError('You did not send a device')
            if post['command']:
                command=request.form['command']
            else:
                raise ValueError('You did not send a command')
        else:
            raise ValueError('Please POST a device and command')
        data = device_read(device, command)
    except Exception as e:
        errors = str(e)
    output = OrderedDict([('device', device), ('command', command), ('data', data), ('errors', errors)])
    return json.dumps(output)

def device_read(device_name, cmd):
    global devices
    count=0
    for i in devices:
        if devices[count].getName() == device_name:
            data = devices[count].getData(cmd)
        count+=1
    return data

def init_devices():
    global devices
    device_names = device.DEVICE_NAMES
    for i in device_names:
        devices.append(Device(i))


if __name__ == "__main__":
    init_devices()
    app.run(host= ('0.0.0.0'), threaded=True)

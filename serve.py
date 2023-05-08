from flask import Flask

import subprocess
import socket
import os

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def run_stress_cpu():
   p = subprocess.Popen(["python3", stress_cpu.py], stdout=subprocess.PIPE)

@app.route('/',methods = ['GET'])
def get_seed():
   hostname = socket.gethostname()
   ip = socket.gethostbyname(hostname)
   return ip

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug = True)


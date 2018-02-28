import socket
import os
import sys
import time
import logging

from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      pod_hostname = socket.gethostname()
      cur_time = time.ctime()
     
      logging.basicConfig(filename='example.log',level=logging.DEBUG)
      logging.info(pod_hostname + ' ' + cur_time + '\n')

      ex  = open('example.log', 'r')
      oc_log = ex.readline()

      return render_template('hello.html',
                          pod_hostname=pod_hostname,
                          cur_time=cur_time,
                          log=oc_log) 
    except:
      return "Hello World! Greetings from "+socket.gethostname() + "\n"
      pass


if __name__ == "__main__":
    application.run(debug=True)

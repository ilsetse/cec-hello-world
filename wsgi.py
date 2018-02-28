import socket
import os
import sys
import time
import logging

from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      pod_hostname = socket.gethostname()
      cur_time = time.ctime()
      pvc1 = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'),'app.log')
      logging.basicConfig(filename=pvc1,level=logging.DEBUG)
      logging.info(pod_hostname + ' ' + cur_time + '\n')
      ex  = open(pvc1, 'r')
      oc_log = ex.readline()
      return "Hello World! Greetings from " + socket.gethostname() + "   Log: " + oc_log + "\n"
    except:
      pass


if __name__ == "__main__":
    application.run(debug=True)

import socket
import os
from datetime import datetime
from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def hello():
    try:
      pod_hostname = socket.gethostname()
      cur_time = str(datetime.now())
      #oc_log = os.env('OPENSHIFT_DATA_DIR')
      return render_template('hello.html',
                          pod_hostname=pod_hostname,
                          cur_time=cur_time)
                          #log=oc_log) 
    except:
      return "Hello World! Greetings from "+socket.gethostname() + "\n"
      pass


if __name__ == "__main__":
    application.run(debug=True)

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
      #logger=logging.getLogger(__name__)
      #logger.setLevel(loggin.NOTICE)

      # file handler
      #handler = logging.FileHandler(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR','app.log')))
      #handler.setLevel(logging.NOTICE)

      # create logging format
      #formatter = logging.Formatter('%(asctime)s')
      #handler.setFormatter(formatter)

      # add handlers to logger
      #logger.addHandler(handler)
      
      
      #logging.basicConfig(format=FORMAT,level=NOTICE)
      #handler = logging.FileHandler(logfile_name)
      #handler.setLevel(logging.notice)


      #print($OPENSHIFT_DATA_DIR)
      oc_log = sys.executable

      return render_template('hello.html',
                          pod_hostname=pod_hostname,
                          cur_time=cur_time,
                          log=oc_log) 
    except:
      return "Hello World! Greetings from "+socket.gethostname() + "\n"
      pass


if __name__ == "__main__":
    application.run(debug=True)

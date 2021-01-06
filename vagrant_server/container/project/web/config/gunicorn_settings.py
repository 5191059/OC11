import os

# UNIXドメインソケット
# socket_path = 'unix:/tmp/gunicorn_socket/gunicorn_flask.sock'
# TCPソケット
socket_path = '0.0.0.0:' + str(os.getenv('PORT', 83))
bind = socket_path

# Debugging
reload = True

# Logging
accesslog = '-'
#loglevel = 'info'
loglevel = 'debug'
logfile = './log/app.log'
logconfig = None

# Proc Name
proc_name = 'Infrastructure-Mechanic-Garage'

# Worker Processes
workers = 1
worker_class = 'sync'
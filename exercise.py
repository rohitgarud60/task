import datetime
import subprocess
import time
cmd = ['./exercise.exe']
while True:
  result = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
  datetime_object = datetime.datetime.now()
  with open('index.html', "w") as f:
    f.write("f<html><body>Hello from python, time: <b>{datetime_object}</b></p>\n")
    f.write("f<p>from C: <b>{result}</b></p></body></html>\n")
time.sleep(5)

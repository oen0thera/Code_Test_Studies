import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
print(type(pst))

print('Current Date time in PST=',datetime.now(pst))

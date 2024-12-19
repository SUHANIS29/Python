#double the wait time after retries
# strting from 1sec and stops sfter 5 sec  
import time
wait_time=1
limit=5
attempt=0
while(attempt<limit):
  print("attempt: \n",attempt+1)
  print("wait time \n",wait_time)
  time.sleep(wait_time)
  wait_time*=2
  attempt+=1
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from whatsapp_bot import automation_function
#def job_function():
    #print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(automation_function, 'interval', seconds=5 )

sched.start()
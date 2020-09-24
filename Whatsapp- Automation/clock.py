from apscheduler.schedulers.blocking import BlockingScheduler
from text import send

sched=BlockingScheduler()

# Schedule send to be called every 2 hours
sched.add_job(send,'interval',seconds=3600)

sched.start()
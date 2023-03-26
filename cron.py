from crontab import CronTab
import time

cron = CronTab(user='ths')
cron.remove_all()

check_appointment_job = cron.new(command="python check_appointment.py")
check_appointment_job.minute.on(0)

cron.write()

for result in cron.run_scheduler():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"{current_time}: A job was executed")

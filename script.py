import subprocess
import datetime

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


total_uptime_hours = subprocess.check_output("smartctl -a disk0 -s on| grep Power_On_Hours | awk '{print $10}'", shell=True)

initialize_year = int(subprocess.check_output("ls -la /private/var/db/.AppleSetupDone | awk '{print $8}'", shell=True).decode("utf-8"))
initialize_month = subprocess.check_output("ls -la /private/var/db/.AppleSetupDone | awk '{print $7}'", shell=True).decode("utf-8")
initialize_day = int(subprocess.check_output("ls -la /private/var/db/.AppleSetupDone | awk '{print $6}'", shell=True).decode("utf-8"))

initialize_month = initialize_month.replace('\n', '')
initialize_month_int = int(months.index(initialize_month))

bought_date = datetime.datetime(initialize_year, initialize_month_int, initialize_day)
now = datetime.datetime.now()
delta = now - bought_date

hours_per_day = round(float(total_uptime_hours) / float(delta.days),2)

hours = int(hours_per_day)
minutes = int((hours_per_day-hours) * 60)

answer = ("Since you first turned on this machine (%s %s %s), "
    "it's been on for %d hours, an average of %d hours and %d minutes per day.") % (initialize_day,
        initialize_month, initialize_year, int(total_uptime_hours), hours, minutes)
print (answer)

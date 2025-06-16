
**What are cronjobs?**
A cronjob is a scheduled task in Unix-like operating systems. It allows you to automate the execution of commands or scripts at specified times or intervals. The cron daemon (`cron`) is responsible for running these tasks.

Cron jobs are typically defined in a crontab file, which specifies the time and date when the command should run. Each line in the crontab file represents a single task and includes five time fields followed by a command to execute.

![[Pasted image 20250117122656.png]]

Ex: `0 2 * * * /usr/bin/backup_script.sh`
	This example runs the `/usr/bin/backup_script.sh` script every day at 2:00 AM.

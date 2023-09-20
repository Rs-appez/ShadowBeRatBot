from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os
import config
from datetime import datetime,timedelta, timezone

class Scheduler:
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()
        self.__init_schedule()
        self.__add_jobs()
        self.scheduler.start()

    def __init_schedule(self):
        job_defaults = {"coalesce": False, "max_instances": 3}
        self.scheduler.configure(job_defaults=job_defaults)

    def __add_jobs(self):
        self.scheduler.add_job(self.__clear_tmp, CronTrigger(hour=5))


    async def __clear_tmp(self):   
        path = config.TMP_PATH
        for file in os.listdir(path):
            file_path = f"{path}/{file}"
            stat = os.stat(file_path)
            access_dt = datetime.fromtimestamp(stat.st_atime)
            is_old = datetime.now() - access_dt > timedelta(hours=12)

            if is_old :
                os.remove(file_path)
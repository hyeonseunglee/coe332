# worker.py
from jobs import q, update_job_status, add_worker_IP
import time
import os

## Added for Section B
worker_ip = os.environ.get('WORKER_IP')

@q.worker
def execute_job(jid):
    update_job_status(jid, "in progress")
    ## Added for section B
    add_worker_IP(jid,worker_ip)
    time.sleep(15)
    update_job_status(jid, "complete")


if __name__ == "__main__":
    execute_job()	

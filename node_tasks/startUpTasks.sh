#!/bin/bash

cd /home/thefair/www/WeiboCrawler && /usr/local/bin/python3.6 /bin/celery beat -A tasks.workers -l info & && nohup /usr/local/bin/python3.6 /bin/celery -A tasks.workers -Q login_queue,user_crawler,home_crawler,ajax_home_crawler worker -l info -c 1 &
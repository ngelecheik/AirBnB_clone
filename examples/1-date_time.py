#!/usr/bin/python3
from datetime import timedelta
from datetime import datetime

date_now = datetime.now()
date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow)

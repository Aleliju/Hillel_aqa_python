import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
file_handler = logging.FileHandler('hb_test.log')
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





filtered_log = []
with open('hblog.txt', 'r') as f:
    for line in f:
        if "TSTFEED0300|7E3E|0400" in line:
            pos = line.find("Timestamp ")
            substring = line[pos+10:pos+18]
            time_format = "%H:%M:%S"
            time_object = datetime.strptime(substring, time_format)
            filtered_log.append(time_object)

def diff_between_31_and_33_sec():
    for prev_time, curr_time in zip(filtered_log, filtered_log[1:]):
        prev_seconds = prev_time.hour * 3600 + prev_time.minute * 60 + prev_time.second
        curr_seconds = curr_time.hour * 3600 + curr_time.minute * 60 + curr_time.second
        difference = prev_seconds - curr_seconds
        if 31 < difference < 33:
            logger.warning(f"Heartbeat in range from 31 to 33 seconds = {difference}")
        if difference >= 33:
            logger.error(f"Heartbeat is more than 33 second = {difference}")

diff_between_31_and_33_sec()





#!/usr/bin/env python3
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event

from beautiful_date import *

import sys
import os
import argparse

# This really shouldn't be called "do" lmao


def do(args):
    """The actual main function"""
    task = args.task
    time = args.tim
    # TODO if its malformed, just print the proper error and move on
    _day, _month, _year = int(D.now().day), int(
        D.now().month), int(D.now().year)
    # TODO this will throw two errors, one for missing environment variable and one for missing credentials.json
    calendar = GoogleCalendar(os.environ['SCHEDULE_EMAIL'])
    event = Event(task,
                  start=(_day/M[_month]/_year)[int(time[:2]):int(time[2:])],
                  location="Operation Hope",
                  minutes_before_popup_reminder=30)
    calendar.add_event(event)
    print(f'Created a task called {task} at the time {time}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('task', type=str,
                        help="Task, written between double quotes (\"\")")
    parser.add_argument('time', type=str,
                        help="The start time of the task, should be in military time (example: 0900) (9am))")
    do(parser.parse_args())


if __name__ == '__main__':
    main()


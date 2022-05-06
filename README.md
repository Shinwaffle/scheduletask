# scheduletask
Script to quickly create google calendar events from the command line. I created this script as a means to quickly jot down ideas for later. Pulling up GNOME Calendar and using my moues is *of course* too much work.
# Requirements

## Google Calendar Simple API

https://github.com/kuzmoyev/google-calendar-simple-api

`pip install gcsa`

## Beautiful Date

https://github.com/kuzmoyev/beautiful-date

`pip install beauitful-date`

You also need an enviroment variable called "SCHEDULE_EMAIL" with your email.
How to create one on linux as an example: `export SCHEDULE_EMAIL="example@example.org"`

# Roadmap:
Overall just more customization of the event itself, also have the ability to create recurring tasks. Also, make this a package.

# scheduletask
Script to quickly create google calendar events from the command line. I created this script as a means to quickly jot down ideas for later. Pulling up GNOME Calendar and using my moues is *of course* too much work.

I'm working on a PyPI release soon, didn't realize I couldn't just *upload* it and it works. I thought computers were magic, damnit!
# Requirements

## Google Cloud Project
You can install the package on PyPI:

`pip install -U scheduletask`

Once downloaded, follow the Prerequisites in this link : https://developers.google.com/calendar/api/quickstart/python. The downloaded credentials should be renamed to credentials.json.

On Windows, they should be put in as: `C:\Users\$USER\.credentials\credentials.json`
(If your windows installation is not on C: but on D: (or X:, so on) put it there)

On Linux, they should be put in as:
`/home/$USER/.credentials/credentials.json`

On Mac, they should be put in as:
`/Users/$USER/.credentials/credentials.json`

## Google Calendar Simple API

https://github.com/kuzmoyev/google-calendar-simple-api

`pip install gcsa`

### Note for Mac

When testing this in a vm, I had to download this library with `sudo` privileges.
Either my vm is not setup right, or that's just what you have to do.

## Beautiful Date

https://github.com/kuzmoyev/beautiful-date

`pip install beauitful-date`

You also need an enviroment variable called "SCHEDULE_EMAIL" with your email. These are instructions on how to create them temporarily for the means of testing.

How to create one on Linux/Mac: 
`export SCHEDULE_EMAIL="example@example.org"`
To make it persistent, add that line to your .bashrc/.zshrc (either/or)

How to create one on Windows (Powershell):
`$env:SCHEDULE_EMAIL = "example@example.org"`
To make it persistent, in a Powershell session:
``[Environment]::SetEnvironmentVariable('SCHEDULE_EMAIL', 'YOUR_EMAIL', 'MACHINE')``
Replace `YOUR_EMAIL` with your actual email.

# Roadmap:
How to setup PATH to execute from command line.
Perhaps provide detailed instructions on getting your `credentials.json`.
Create a config argument to store remind time, etc.
Also, timezones seem to be kinda weird with it.
Create some GitHub Actions workflows to automate package publishing alongside testing (For Windows, Linux, and Mac(Soon)).
Also, add a whole bunch of more features (obviously) alongside pip automatically installing gcsa and beautiful-date (I'm too dumb to do it right now)

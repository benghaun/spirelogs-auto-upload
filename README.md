# spirelogs-auto-upload
This is a command line tool for automatic uploading of Slay the Spire run files to Spirelogs built using Python. It is basically a simpler version of Zurkei's implementation (located at https://github.com/Zurkei/SpireLogsUploader). Zurkei's implementation has a GUI while this version is purely CLI. 

## Installation and configuration
This tool has been tested to run on Python 3.6. 


In order to use this tool, enter your Spirelogs username, Spirelogs password, and path to run files in config.py. Username and password can be left as `None` if you wish to upload your runs anonymously. 

You also need to install the requirements:

`pip install -r requirements.txt`

## Usage

This tool does two things: the first of which is to upload all existing run files. To do so, run main.py with the --upload flag:

`python main.py --upload`

The other is to automatically upload new run files whenever they are created (i.e whenever you complete a run). To do so, simply run main.py without the --upload flag:

`python main.py`

The recommended method to use this tool would be to configure this process to run in the background all the time, which can be done using the Task Scheduler for Windows (configure the script to run on startup) or Supervisor for Unix/Linux systems. 

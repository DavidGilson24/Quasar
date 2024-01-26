# Setting up the bot (preferably on 

### Install python:

First off, updating and apt installing python:
`$ sudo apt-get update
 $ sudo apt-get install python3`

Verify python is installed:
` python3 --version`

### Install PIP (on UNIX):

Installing command:
`sudo apt install python3-pip`

Verifying installation:
`pip3 help`
or
`pip help`

### Starting virtual environment:

Navigate to the working repostory (your project folder), and run the following:
`python -m venv openai-env`

And now to activate (on UNIX or Mac):
`source openai-env/bin/activate`

And to activate on Windows:
`openai-env\Scripts\activate`

### Installing the library:

Download the Python OpenAI library (DO THIS ONCE V.ENV IS ON):
`pip install --upgrade openai`

### Set API key:

Run this code:
`setx OPENAI_API_KEY "your-api-key-here"`

If this didn't work, implement the API key as an environnment variable.


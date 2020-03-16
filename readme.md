# Note for windows users
Ensure to tick the option to include python in your system PATH during installation. If some commands do not run try uninstalling python and installing again with the option selected.

Use Windows PowerShell as python virtual environment commands will vary depending on your shell. If you are using another shell check the documentation first: https://docs.python.org/3/library/venv.html

Use `python3` and `python` commands interchangeably depending on your installation. Use whichever one successfully pints the version. 

# Dependencies
These instructions assume that you have at least python3 version 3.7.4 and npm version 6.5.0 installed. Check by running ```python3 --version``` and ```npm --version``` from the command line.

# 1. Setup your environment 
In your terminal window, navigate to the root directory of this repository (where this readme is) and execute all of the following commands.
- ```python3 -m venv venv``` 
- ```venv/Scripts/Activate.ps1``` on windows or ```source venv/bin/activate``` on linux or MacOS
- ```pip install flask``` 
- ```pip install python-dotenv```
- ```npm install -g sass``` on windows or ```sudo npm install -g sass``` on linux or MacOS
- ```npm install -g nodemon``` on windows or ```sudo npm install -g nodemon``` on linux or MacOS

# 2. Start the nodemon listeners
Start two terminal windows and navigate to the root directory of this repository in both.
- Depeding on your OS run ```source venv/bin/activate``` or ```venv/Scripts/Activate.ps1``` in both terminals to activate the virtual environment
- Run ```nodemon -x "flask run" -e py,html,css``` in the first window
- Run ```nodemon -x "sass scss/custom.scss app/static/styles/custom_bootstrap.css" -e scss``` in the second window
- Ensure to keep both processes running while you are developing your application

# 3. Verify the webserver is running and nodemon is watching for changes
- Open your browser and go to http://localhost:5000/
- Make an edit in the `scss/custom.scss` file and check that sass recompiled in the terminal after you save the changes.
- Finally do a hard refresh in your browser and check that the changes are available in your flask app. (ensure to empty cache and hard reload because css files are chached).

# If you just want to compile your own Bootstrap
- ensure you have npm v 6.5.0 installed
- Run ```npm install -g sass``` on windows or ```sudo npm install -g sass``` on linux or MacOS
- Edit the ```scss/custom.scss``` file
- Run ```sass scss/custom.scss app/static/styles/custom_bootstrap.css``` from the root directory
- Your custom Bootstrap .css will be generated at ```app/static/styles/custom_bootstrap.css```


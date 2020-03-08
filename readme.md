# Dependencies
These instructions assume that you have at least python3 version 3.7.4 and npm version 6.5.0 installed. Check by running ```python3``` and ```npm --version``` from the command line.

# 1 Setup your environment 
In your terminal window, navigate to the root directory of this repository (where this readme is) and execute all of the following commands.
- ```python3 -m venv venv``` 
- ```source venv/bin/activate``` 
- ```pip install flask``` 
- ```pip install python-dotenv`` 
- ```pip install wdb``` 
- ```pip install wdb.server`` 
- ```npm install -g sass``` 
- ```npm install -g nodemon``` 

# 2 Start the local debug server
- ```wdb.server.py &``` only need to do this once between computer restarts, debug server will run as a background process.

# 3 Let nodemon do all the work for you
Start two terminal windows and navigate to the root directory of this repository in both.
- Run ```nodemon -x "flask run" -e py,html,css``` in the first window
- Run ```nodemon -x "sass scss/custom.scss app/static/styles/custom_bootstrap.css" -e scss``` in the second window
- Ensure to keep both processes running while you are developing your application





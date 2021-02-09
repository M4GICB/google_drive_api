# google_drive_api
__Description:__  
This project is a base Django Project that will allow someone to connect to a Google Drive account, view files the user has access to, download files using a file id, and upload files using a full path name. The home page consists of a few buttons (explained below). Each button provides a different proof of concept for the project. 

* __Button 1:__ Sends a js alert that says "hello"
  * POC: Executing JS through HTML in Django Template
* __Button 2:__ Runs a a function written inside of the `home` template that sends a js alert that says "whats up...?"
  * POC: Executing JS through script tages written in Django Template
* __Button 3:__ Executes python script function to allow a user to see, download and upload files. 
  * POC: Executing functions written in an external python file by clicking buttons in Django Template

## Set up
* A few modules need to be installed to get this code working.
* Run the following commands to make sure nessesary modules are installed:  
`pip3 install google-api-python-client`   
`pip3 install google-auth google-auth-oauthlib`
* A credentials.json is also needed for this project to work.
  * Be sure to get the credentials file nessesary to connect to your Google Drive Account. 

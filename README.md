This is a text based application that allows users to create an account and login. The application uses SQLite to store
the usernames and passwords. The passwords on the database are stored in a SHA256 encryption scheme. I've created this 
project as a part of my learning in order to store persistent data and recall that data. The first logical step of this
for me was to create a system in which users could login. 

My next step would be to add to the database and allow for data to be stored within the database. I'm debating on making
this a "to do" list. It seems to be a popular project. 

For this project I am doing my best to steer clear of a tutorial that just shows me how to do it and am looking for ways 
to solve roadblocks with my own research and discovery. 


Current functionality:
1. Able to make a user with a password, and convert the password to SHA256.
2. Able to create database with a table named users.
3. Table stores a username and a password.
4. Able to create users and store their username and password in the database. 
5. Need to be able to check the username and password against the value stored in the database and authenticate or
decline the login. 
6. create some functionalities to do once logged in.
   - able to add and store notes to the database.


Currently working on:
A way to view notes that have been stored in the database.
  

next steps:
1. Make sure user's can't see other user's data.
3. Put some rules around password creation, currently a password like "123456" is considered valid. I would like to add
standard requirements like requiring capitals, lowercase, numbers and symbols in the password generation or asking for
the user to enter a different password that fulfils the requirements. 
4. Migrate this to a GUI framework, with either TKinter or PyQT5. 
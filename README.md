This is a text based application that allows users to create an account and login. The application uses SQLite to store
the usernames and passwords. The passwords on the database are stored in a SHA256 encryption scheme. I've created this 
project as a part of my learning in order to store persistent data and recall that data. The first logical step of this
for me was to create a system in which users could login. 

I've added a "note" functionality that allows users to make notes and add it to their data when logged in. I've designed
this so that users can only see the notes that they have made based on how it is queried in the database. 


NOTE:
For this project I am doing my best to steer clear of a tutorial that just shows me how to do it and am looking for ways 
to solve roadblocks with my own research and discovery. I have found a lot of good basic information that I have been 
able to adapt from the https://www.sqlitetutorial.net/ website. Their tutorial is in the same vein as this project but 
is different enough that I've been able to write my own code and problem solve using the examples provided as a 
baseline. I feel like this project has helped me personally get a better understanding of how my own code works and it
is not highly dependent on just copy/pasting from things I've found online. 


Current functionality:
1. Able to make a user with a password, and convert the password to SHA256.
2. Able to create database with a table named users.
3. Table stores a username and a password.
4. Able to create users and store their username and password in the database. 
5. Need to be able to check the username and password against the value stored in the database and authenticate or
decline the login. 
6. create some functionalities to do once logged in.
   - Able to add and store notes to the database.
   - Added a way to view notes that have been stored in the database.
     - Make sure user's can't see other user's data. Based on how the information is queried, users cannot see each 
     other's data. 
   - Adding functionality to edit and delete notes. 
7. Added a help section for once the user is logged in with commands they can use.

Currently, working on:
Looking into the best way to convert this to a GUI. Will likely spin that off in a separate repo.  

next steps:

1Put some rules around password creation, currently a password like "123456" is considered valid. I would like to add
standard requirements like requiring capitals, lowercase, numbers and symbols in the password generation or asking for
the user to enter a different password that fulfils the requirements. 
2Migrate this to a GUI framework, with either TKinter or PyQT5. 
 

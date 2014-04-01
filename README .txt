VirtualFittingRoom
==================

CS169 Spring 2014
 
The code for iteration 1 is in the iter1 branch
1. To run the server on the local machine, please clone the iter1 branch from github and call "python manage.py runserver" under the VirtualFittingRoom directory.

2. To run the test, please under the same directory and call " python manage.py test"

3. The latest app has been deployed to Heroku, the link is: 
	http://virtualfittingroom.herokuapp.com






For Iteration2:

   1. To use the selenium GUI automation tests, open the $DRIVER_HOME as a package in Eclipse since the tests are written in java. In the run configuration, create a new java application, add "$WEBDRIVER_HOME" to the project blank and add "org.openqa.selenium.example.Example"to the main class blank. Then click run.
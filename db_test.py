import sqlite3 #imports DB ability
import unittest #imports ability to test
from unittest.mock import patch #imports ability to patch a mock


  @mock.patch(sqlite3)  #tells program to create a mock object to act in place of sqlite3
def test_main(self, mock_db): #a test function that talks to itself and the mock_db sqlite3)
  
	##TODO Add [] to db so that assertion passes
    sqlite_db = sqlite3.connect('database.sqlite')#creates db that connects to mock db
	assert(sqlite_db[0] == 'Two') #asserts that the fake index is identical
	
  
  

if __name__ == '__main__': #tells computer not to auto start main. Reminds code to check name. 
    main()
import sqlite3
import unittest

  @mock.patch(sqlite3) 
def test_main(self, mock_db):
  
	##TODO Add [] to db so that assertion passes
    sqlite_db = sqlite3.connect('database.sqlite')
	assert(sqlite_db[0] == 'Two')
	
  
  

if __name__ == '__main__': #tells computer not to auto start main. Reminds code to check name. 
    main()
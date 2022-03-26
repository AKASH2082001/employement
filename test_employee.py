import unittest

import sqlite3 as sql

class testing_Employee(unittest.TestCase):

    def setUp(self):
        self.name= "akash"
        self.code = "8"
        self.connection=sql.connect("company.db")

    def tearDown(self):
        self.name=" "
        self.salary=" "
        self.connection.close()

    def test_verify_Employee(self):
        result = self.connection.execute("select employee_name from Employee where employee_name="+self.code)
        for i in result:
            fetchedemployeename= i[0]
            self.assertEqual(self.name,fetchedemployeename)

if __name__ == "__main__":
    unittest.main()
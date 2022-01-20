import unittest  # Importing the unittest module
from users import Users


class TestUsers(unittest.TestCase):
    '''
    Test class that defines test cases for the Users class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = Users("Jimmy", "1234")

    def test_initialization(self):
        '''
        test_initialization case to test whether the object is being initialised properly
        '''
        self.assertEqual(self.new_user.username, "Jimmy")
        self.assertEqual(self.new_user.login_password, "1234")

    def test_add_user(self):
        '''
        test_add_user test case to test if the contact object is saved into the users list
        '''
        self.new_user.add_user()
        self.assertEqual(len(Users.users_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Users.users_list = []

    def test_add_multiple_users(self):
        '''
        test_add_multiple_users to check if we can save multiple user objects to our users_list
        '''
        self.new_user.add_user()
        test_user = Users("Apple", "2022")
        test_user.add_user()
        self.assertEqual(len(Users.users_list), 2)

    def test_remove_users(self):
        '''
        test_remove_users to test if we can remove a user from our user list
        '''
        self.new_user.add_user()
        test_user = Users("Apple", "2022")
        test_user.add_user()
        test_user1 = Users("Wanyutu", "1234")
        test_user1.add_user()

        test_user.delete_user()
        self.assertEqual(len(Users.users_list), 2)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username
        '''
        self.new_user.add_user()
        test_user1 = Users("mike", "1234")
        test_user1.add_user()

        found_user = Users.find_by_username("Jimmy")
        self.assertEqual(found_user.login_password, test_user1.login_password)

    def test_user_exists(self):
        '''
        test to see if a true is returned when a user exists and false otherwise
        '''
        self.new_user.add_user()
        test_user = Users("Jimmy", "1234")
        test_user.add_user()

        user_exists = Users.user_exists("Jimmy", "1234")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()

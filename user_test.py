import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = User(
            "Jimmy", "Jammie", "0712345678", "jimmy@ms.com")  # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "Jimmy")
        self.assertEqual(self.new_contact.last_name, "Jammie")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "jimmy@ms.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the user list
        '''
        self.new_contact.save_contact()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)
# setup and class creation up here

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our user_list
        '''
        self.new_contact.save_contact()
        test_contact = User("Jimmy", "Jammie", "0712345678",
                            "jimmy@ms.com")  # new contact user
        test_contact.save_contact()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_contact(self):
        '''
       test_delete_contact to test if we can remove a contact from our user list
         '''
        self.new_contact.save_contact()
        test_contact = User("Jimmy", "Jammie", "0712345678",
                            "jimmy@ms.com")  # new contact
        test_contact.save_contact()

        self.new_contact.delete_contact()  # Deleting a contact object
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()

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


if __name__ == '__main__':
    unittest.main()

import pyperclip
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

        # Deleting a contact object
        self.new_contact.delete_contact()  # Deleting a contact object
        self.assertEqual(len(User.user_list), 1)

    def test_find_contact_by_number(self):
        '''
         test to check if we can find the user  by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = User("Jimmy", "Jammie", "0711223344",
                            "jimmy@ms.com")  # new contact
        test_contact.save_contact()

        found_contact = User.find_by_number("0711223344")
        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        '''
         test to check if we can return a Boolean if we cannot find the contact.
        '''
        self.new_contact.save_contact()
        test_contact = User("Jimmy", "Jammie", "0711223344",
                            "jimmy@ms.com")  # new contact
        test_contact.save_contact()
        contact_exists = User.contact_exist("0711223344")
        self.assertTrue(contact_exists)
        self.assertTrue(contact_exists)
        '''
        method that returns a list of all contacts saved in the user_list
        '''

        self.assertEqual(User.display_contacts(), User.user_list)

    def test_display_all_contacts(self):
        '''
        method that returns a list of all users saved
       '''

        self.assertEqual(User.display_contacts(), User.user_list)

    def test_copy_email(self):
        '''
          Test to confirm that we are copying the email address from a found user
          '''

        self.new_contact.save_contact()
        User.copy_email("0712345678")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()

import random
import string

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__ (self, application_name, account_username, account_password):
        '''
        __init method that helps us define properties for our objects

        Args:
        application_name: New application name
        account_username: New account username
        account_password: New account password
        '''
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password

    def add_credentials(self):
        '''
        add_credentials method that saves credentials into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method that removes credentials from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of all credentials
        '''
        return Credentials.credentials_list

    @classmethod
    def find_by_application_name(cls, application_name):
        '''
        Method that takes in an application name and returns the credentials for the said application

        Args:
        application_name: name of application credentials to be found

        Returns:
        Credentials of the application
        '''
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return credential
    
    @classmethod
    def credentials_exist(cls, application_name):
        '''
        Method that checks if a credential exist from credentials_list

        Args:
        application_name : name to search if account exists

        Return:
        Boolean
        '''
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return True
        return False

    @staticmethod
    def generate_password(passwordLength):
        '''
        method that generates a random password for the user
        '''
        random_alphanumeric = string.ascii_letters + string.digits
        password = ''.join((random.choice(random_alphanumeric) for i in range(passwordLength)))
        return password

    
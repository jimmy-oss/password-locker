class User:
    """
    Class that generates new instances of users.
    """

    user_list = []  # Empty user list

    def __init__(self, first_name, last_name, number, email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
# always remember to import e.g from user import User
# Init method up here
    user_list = []  # Empty user list
    # Init method up here

    def save_contact(self):
        '''
        save_contact method saves contact objects into  the user_list
        '''
        User.user_list.append(self)

class Users:
    '''
    Class that generates new instances of users
    '''
    users_list = []

    def __init__ (self, username, login_password):
        '''
        ___init___ method that helps us define properties for our objects.
        Args: 
        username: New username
        login_password: New user password
        '''
        self.username = username
        self.login_password = login_password
    
    def add_user(self):
        '''
        add user details method saves user object into users list
        '''
        Users.users_list.append(self)

    def delete_user(self):
        '''
        delete user details method removes user object from users list
        '''
        Users.users_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        authenticate user username

        Args: 
        username : name used by user to login

        Returns: 
        user
        '''
        for user in Users.users_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username, login_password):
        '''
        authenticate user username and password by checking if user exists in the users list

        Args: 
        username : name used by user to login
        login_password: password for the user

        Returns: 
        boolean
        '''
        for user in Users.users_list:
            if user.username == username and user.login_password == login_password:
                return True
        return False
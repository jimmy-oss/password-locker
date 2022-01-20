#!/usr/bin/env python3
from users import Users
from credentials import Credentials


def create_user(username, login_password):
    '''
    Function to create new user
    '''
    new_user = Users(username, login_password)
    return new_user


def add_user(user):
    '''
    Function to save user
    '''
    user.add_user()


def remove_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()


def find_user(username):
    ''' 
    Function to find user by username
    '''
    return Users.find_by_username(username)


def check_existing_user(username, login_password):
    ''' 
    Function to authenticate user
    '''
    return Users.user_exists(username, login_password)


def create_credentials(application_name, account_username, account_password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(
        application_name, account_username, account_password)
    return new_credentials


def add_credentials(new_credentials):
    '''
    Function to save credentials
    '''
    new_credentials.add_credentials()


def remove_credentials(new_credentials):
    '''
    Function to delete credentials
    '''
    new_credentials.delete_credentials()


def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_credentials()


def check_existing_credentials(application_name):
    '''
    Function to check that credentials for a certain application exist
    '''
    return Credentials.credentials_exist(application_name)


def find_credentials(application_name):
    '''
    Function that finds credentials using the application name
    '''
    return Credentials.find_by_application_name(application_name)


def generate_a_password(passwordLength):
    '''
    Function that generates random password of 8 characters
    '''
    return Credentials.generate_password(passwordLength)


def main():
    print(" "*8 + "✧  🎀  𝓅𝒶𝓈𝓈𝓌🍪𝓇𝒹 𝓁🌸𝒸𝓀𝑒𝓇  🎀  ✧" + " "*8)
    print("--"*24)
    print("An application that manages your passwords.")
    while True:
        print("What is your name?")
        current_user = input().strip(' ').capitalize()
        if current_user != '':
            print(f"\nHello👋 {current_user},")
            while True:
                print("Kindly use these short codes to navigate the application🤗 : \n CA - create an account \n SI - sign into an existing account \n DA - delete your account \n EX - exit the application ")
                short_code = input().upper()

                if short_code == 'CA':
                    print("\nCREATE AN ACCOUNT")
                    print("-"*17)
                    print("Enter a name you wish to use as your username")
                    print(
                        " "*4 + "*the username must contain alphabetical letters only and no spaces*")

                    while True:
                        username = input().capitalize()
                        if username.isalpha():
                            print("Enter a password for your account")
                            print(
                                " "*4 + "*the password must be 6 characters or longer*")
                            while True:
                                login_password = input()
                                if len(login_password) >= 6:
                                    add_user(create_user(
                                        username, login_password))
                                    print(
                                        f"\nAccount for {username} has been successfully created.\nProceed to sign in.\n")
                                    break
                                else:
                                    print(
                                        "\nThe password you entered is too short.")
                                    print(
                                        "Please use a password of 6 characters or more.")
                                    continue

                        else:
                            print("\nThe username you entered is not valid.")
                            print(
                                "Please use alphabetical letters only with no spaces.")
                            continue
                        break

                elif short_code == 'SI':
                    print("\nSIGN IN")
                    print("-"*7)

                    print("Enter your username")
                    username = input().strip(' ').capitalize()
                    print("Enter your password")
                    login_password = input().strip(' ')

                    if check_existing_user(username, login_password):
                        print("\nLog in successful")
                        print("What would you like to do?")

                        while True:
                            print("\nUse these short codes for navigation🤗 : \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
                            credentials_navigation = input().upper()

                            if credentials_navigation == 'CC':
                                print("\nCREATE NEW CREDENTIALS")
                                print("-"*22)
                                while True:
                                    print("Application name:")
                                    print(" "*4 + "*eg. Twitter*")
                                    application_name = input().capitalize().strip(' ')
                                    if application_name != '':
                                        print(
                                            f"What is your current/desired username on {application_name}?")
                                        account_username = input()

                                        while True:
                                            print(
                                                f"\nDo you already have a password for your account on {application_name}? (Y/N)")
                                            has_password = input().upper()
                                            if has_password == 'Y':
                                                print(
                                                    f"Enter your {application_name} password")
                                                account_password = input()
                                                add_credentials(create_credentials(
                                                    application_name, account_username, account_password))
                                                print(
                                                    f"\nAccount credentials for your {application_name} account have been successfully saved.")
                                                break

                                            elif has_password == 'N':
                                                while True:
                                                    print(
                                                        "Would you like a generated password? (Y/N)")
                                                    gen_pass = input().upper()
                                                    if gen_pass == 'Y':
                                                        print(
                                                            "How long would you like your password to be?")
                                                        print(" "*4 + "less than 8 characters: WEAK" + "\n" + " "*4 +
                                                              "8 characters: STRONG" + "\n" + " "*4 + "8-26 characters: VERY STRONG")
                                                        while True:
                                                            try:
                                                                passwordLength = int(
                                                                    input())
                                                                if passwordLength in range(27):
                                                                    account_password = generate_a_password(
                                                                        passwordLength)
                                                                    print(
                                                                        f"Password generated is {account_password}")
                                                                    add_credentials(create_credentials(
                                                                        application_name, account_username, account_password))
                                                                    print(
                                                                        f"Account credentials for your {application_name} account have been successfully saved.\n")
                                                                    break
                                                            except ValueError:
                                                                print(
                                                                    "\nYou did not pick a valid password length")
                                                                print(
                                                                    "Please pick a number between 0-26 and try again")
                                                                continue
                                                    elif gen_pass == 'N':
                                                        print(
                                                            f"Enter a password you wish to use for your {application_name} account")
                                                        print(
                                                            " "*4 + "*password must be longer than 6 characters*")
                                                        while True:
                                                            account_password = input()
                                                            if len(account_password) >= 6:
                                                                add_credentials(create_credentials(
                                                                    application_name, account_username, account_password))
                                                                print(
                                                                    f"Account credentials for your {application_name} have been successfully saved.\n")
                                                                break
                                                            else:
                                                                print(
                                                                    "\nThe password you entered is too short.")
                                                                print(
                                                                    "Please use a password of 6 characters or more.")
                                                                continue
                                                    else:
                                                        print(
                                                            "You did not select a valid option")
                                                        print(
                                                            "Please enter (Y/N) and try again")
                                                        continue
                                                    break

                                            else:
                                                print(
                                                    "You did not select a valid option")
                                                print(
                                                    "Please enter (Y/N) and try again")
                                                continue

                                            break
                                        break
                                    else:
                                        print(
                                            "\nSorry, I didn't quite get the application name. Please try again.")
                                        continue

                            elif credentials_navigation == 'FC':
                                if len(Credentials.credentials_list) >= 1:
                                    print("\nFIND CREDENTIALS")
                                    print("-"*16)
                                    print(
                                        "Enter the application whose credentials you'd like to find:")
                                    print(" "*4 + "*eg. Twitter*")
                                    searched_application = input().capitalize()

                                    if check_existing_credentials(searched_application):
                                        searched_credential = find_credentials(
                                            searched_application)
                                        print(
                                            f"\nApplication name: {searched_credential.application_name}, \n username: {searched_credential.account_username} \n password: {searched_credential.account_password}")

                                    else:
                                        print(
                                            f"\nThe credentials for {searched_application} don't exist.")

                                    continue

                                else:
                                    print(
                                        "\nYou don't seem to have any credentials saved.")
                                    continue

                            elif credentials_navigation == 'DC':
                                if len(Credentials.credentials_list) >= 1:
                                    print("\nDELETE CREDENTIALS")
                                    print("-"*18)
                                    print("Application name:")
                                    print(" "*4 + "*eg. Twitter*")
                                    application_name = input().capitalize()

                                    if check_existing_credentials(application_name):
                                        while True:
                                            print(
                                                f"Are you sure you want to delete credentials for your {application_name}? (Y/N)")
                                            delete_credential = input().upper()
                                            if delete_credential == 'Y':
                                                remove_credentials(
                                                    find_credentials(application_name))
                                                print(
                                                    f"\nCredentials for {application_name} have been successfully deleted")
                                                break
                                            elif delete_credential == 'N':
                                                print(
                                                    "\nPhew! Your credentials are still intact.")
                                                break
                                            else:
                                                print(
                                                    "You did not select a valid option")
                                                print(
                                                    "Please enter (Y/N) and try again\n")
                                                continue

                                    else:
                                        print(
                                            f"\nCredentials for {application_name} don't exist.")
                                        continue

                                else:
                                    print(
                                        "\nYou don't seem to have any credentials saved.")
                                    continue

                            elif credentials_navigation == 'SC':
                                if len(Credentials.credentials_list) >= 1:
                                    display_credentials
                                    print("\nHERE ARE ALL YOUR CREDENTIALS")
                                    print("-"*29)
                                    for credential in display_credentials():
                                        print(
                                            f"\nApplication name: {credential.application_name} \n Username: {credential.account_username} \n Password: {credential.account_password}")
                                    continue
                                else:
                                    print(
                                        "\nYou don't seem to have any credentials saved.")
                                    continue

                            elif credentials_navigation == 'LO':
                                print("\nYou have successfully logged out..\n")
                                break

                            else:
                                print("\nYou did not select a valid option.")
                                print("Please try again.")
                                continue

                    else:
                        print("\nInvalid username and password")
                        print("Try again or create an account\n")
                        continue

                elif short_code == 'DA':
                    if len(Users.users_list) >= 1:
                        print("\nDELETE YOUR ACCOUNT")
                        print("-"*19)
                        print("Enter your username")
                        username = input().capitalize()
                        print("Enter your password")
                        login_password = input()

                        if check_existing_user(username, login_password):
                            while True:
                                print(
                                    f"Are you sure you want to delete your account? (Y/N)")
                                delete_account = input().upper()
                                if delete_account == 'Y':
                                    remove_user(find_user(username))
                                    print(
                                        f"\nYour account has been successfully deleted.\n")
                                    break
                                elif delete_account == 'N':
                                    print(
                                        "\nPhew! Your account is still active.\n")
                                    break
                                else:
                                    print("You did not select a valid option")
                                    print("Please enter (Y/N) and try again")
                                    continue

                        else:
                            print(
                                "\nSeems like you do not have an active account or you entered the wrong details.")
                            print("Please try again.\n")
                            continue

                    else:
                        print(
                            "\nSorry, there are no active accounts at the moment.\n")
                        continue

                elif short_code == 'EX':
                    print("\nBye👋....")
                    break

                else:
                    print("\nYou did not select a valid option.")
                    print("Please try again.\n")
                    continue

        else:
            print("\nSorry, I didn't quite get your name. Please try again")
            continue

        break


if __name__ == '__main__':
    main()

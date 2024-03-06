import json
import os
import random
import sys

saved_logins = {}
saved_address = {}
saved_banking_info = {}

DATA_FILE = 'save_data.json'

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        saved_data = json.load(file)
        saved_logins = saved_data.get('logins', {})
        saved_address = saved_data.get('address', {})
        saved_banking_info = saved_data.get('banking_info', {})

def save_data_to_file():
    data_to_save = {
        'logins': saved_logins,
        'address': saved_address,
        'banking_info': saved_banking_info
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data_to_save, file)

def user_selection():
    save_login = input('Welcome to Dorians Digits! Your friendly, safe, secure password manager. Would you like to save a login, generate a new one, save personal information, or see your saved data and logins')
    if save_login in ['1', 'One', 'one', 'Save Login', 'Save login', 'save login']:
        login_saver()
    if save_login in ['2', 'two', 'Two', 'Generate Login', 'Generate login', 'generate login', 'Generate a new one', 'generate a new one']:
        generate_passwords()
    if save_login in ['3', 'Three', 'three', 'Save Personal Information', 'Save personal information', 'save personal information', 'Personal Information', 'Personal information', 'personal information']:
        personal_information_selection()
    if save_login in ['4', 'four', 'Four', 'See all saved logins', 'see all saved logins', 'See saved logins', 'see saved logins', 'See logins', 'see logins', 'See Login', 'See logins', 'see login']:
        see_saved_logins()
    if save_login in ['5', 'five', 'Five', 'See saved personal information', 'see saved personal information', 'See saved personal info', 'see saved personal info', 'See Personal Information', 'See personal information', 'see personal information', 'See Information', 'See information', 'see information', 'See Address', 'See address', 'see address', 'See Banking Information', 'See banking information', 'see banking information', 'See Banking Info', 'See banking info', 'see banking info']:
        personal_information_selection()
    elif save_login in ['6', 'six', 'Six', 'Exit Application', 'Exit application', 'exit application', 'End Application', 'End application', 'end application', 'Exit', 'exit', 'End', 'end']:
        save_option = input('Do you want to save your data before exiting? (yes/no): ')
        if save_option.lower() == 'yes':
            save_data_to_file()
        sys.exit()

def handel_user_options():
    option = input('What would you like to do now? ')
    if option in ['1', 'One', 'one', 'Save Login', 'Save login', 'save login']:
        login_saver()        
        login_saver()
    elif option in ['2', 'two', 'Two', 'Generate Login', 'Generate login', 'generate login', 'Generate a new one', 'generate a new one', 'Generate password', 'Generate password', 'generate password']:
        generate_passwords()
    elif option in ['3', 'three', 'Three', 'See all saved logins', 'see all saved logins', 'See saved logins', 'see saved logins', 'See logins', 'see logins']:
        see_saved_logins()
    elif option in ['4', 'four', 'Four', 'Exit Application', 'Exit application', 'exit application', 'End Application', 'End application', 'end application', 'Exit', 'exit', 'End', 'end']:
        save_option = input('Do you want to save your data before exiting? (yes/no): ')
        if save_option.lower() == 'yes':
            save_data_to_file()
        sys.exit()
    else:
        print('Invalid option.')

def generate_passwords():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*()_+-=[]{}|;:,.<>/?~'
    number = int(input('Amount of passwords: '))
    length = int(input('Length of password: '))
    special = input('What special characters would you like to delete: ')
    numbers = input('What numbers would you like to delete: ')
    lowercase = input('What lowercase letters would you like to delete: ')
    capitals = input('What capital letters would you like to delete: ')

    for pwd in range(number):  
        password = ''
        for pwd in range(length):
            char = random.choice(chars)
            if char not in special and char not in numbers and char not in lowercase and char not in capitals:
                password += char
        print(password)
        save_generated_password = input('Would you like to save this password (make sure to copy and paste the password)')
        if save_generated_password in ['Yes', 'yes', 'Y', 'y', 'Save Password', 'Save password', 'save password']:
            login_saver()
        
def login_saver():
    print('Enter the login you would like to save:')
    domain = input('What domain does the login belong to? (e.g. Google, Facebook, Spotify, Steam): ')
    username = input('Username/Email: ')
    password = input('Password: ')

    saved_logins[domain] = {'Username': username, 'Password': password}

def personal_information_selection():
    personal_information = input ('Would you like to save your adress/banking info, or see your saved information?')
    if personal_information in ['1', 'one', 'One', 'Save Address', 'Save address', 'save address', 'Save Billing Address', 'Save billing address', 'save billing address']:
        address_saver()
    if personal_information in ['2', 'two', 'Two', 'Save Banking Information', 'Save banking information', 'save banking information', 'Save Banking Info', 'Save banking info', 'save banking info']:
        bank_saver()
    if personal_information in ['3', 'three', 'Three', 'See Saved Address', 'See saved address', 'see saved address', 'See Address', 'See address', 'see address', 'View Saved Address', 'View saved address', 'view saved address', 'View Address', 'View address', 'view address']:
        see_saved_address()
    if personal_information in ['4', 'four', 'Four', 'See saved banking information', 'see saved banking information', 'See saved banking info', 'see saved banking info', 'See Banking Information', 'See banking information', 'See Banking Info', 'See banking info', 'see banking info']:
        see_saved_banking_info()
        
    

def address_saver():
    address = input('Street Adress: ')
    state = input('State/province: ')
    city = input('City: ')
    zipcode = input('Zipcode: ')
    aptnumber = input('Apartment Number: ')

    saved_address[address] = {'state': state, 'city': city, 'zipcode': zipcode, 'aptnumber': aptnumber}

def bank_saver(): 
    issuer = input('Card Issuer: ')
    name = input('Card Name: ')
    networks = input('Card Network: ')
    account_opening = ('Date of account opening: ')
    experiation = input('Experiation Date: ')
    cardholder_name = input ('Cardholder Name: ')
    number = input('Credit Card Number: ')
    cvv = input('CVV (the three digits on the back of the card): ')

    saved_banking_info[issuer] = {'name': name, 'networks': networks, 'account_opening': account_opening, 'experiation': experiation, 'cardholder_name': cardholder_name, 'number': number,  'cvv': cvv}

def see_saved_logins():
    if not saved_logins:
        print('No saved logins.')
    else:
        print('Saved Logins:')
        for domain, login_info in saved_logins.items():
            print(f'Domain: {domain}, Username/Email: {login_info["Username"]}, Password: {login_info["Password"]}')

def see_saved_address():
    if not saved_address:
        print('No saved personal information.')
    else: 
        print('Saved address: ')
        for address, address_info in saved_address.items():
            print(f'Street Address: {address}, State: {address_info["State/province"]}, City: {address_info["City"]}, Zipcode: {address_info["Zipcode"]}, Apartment Number: {address_info["Apartment Number"]}')

def see_saved_banking_info():
    if not saved_banking_info:
        print('No saved banking information')
    else:
        print('Save banking information: ')
        for issuer, banking_info in saved_banking_info.items():
            print(f'Card Issuer: {issuer}, Card Name: {banking_info["Name"]}, Card Network: {banking_info["Card Network"]}, Date of Account Opening: {banking_info["Date of Account Opening"]}, Expiration Date: {banking_info["Expiration Date"]}, Cardholder Name: {banking_info["Cardholder Name"]}, Credit Card Number: {banking_info["Credit Card Number"]}, CVV: {banking_info["CVV"]},')

user_selection()
personal_information_selection()
handel_user_options()





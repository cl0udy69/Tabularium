def see_address():
    if not save_address:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_address_choices']:
            save_address()
        elif selection.lower() in error_handling_negative['dont_save_address_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print("Invalid Input")
    else:    
        address_info = save_address()
        print('Saved address: ')
        for adress_info in save_address.items():
            print(f'Street Address: {address_info["adress"]}, State/Provice: {address_info["state"]}, City: {address_info["city"]}, Zipcode: {address_info["zipcode"]}, Apartment Number: {address_info["aptnumber"]}')

def see_banking():
    if not save_banking:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_banking_choices']:
            save_banking()
        elif selection.lower() in error_handling_negative['dont_save_banking_choices']:
            choices  = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invlid Input')
    else:
        banking_info = save_banking()
        print('Saved Banking Information: ')
        for banking_info in save_banking.items():
            print(f'Bank: {banking_info["bank"]}, Account: {banking_info["account"]}, Account Type: {banking_info["type"]}, Banking Website: {banking_info["website"]}, Phone Number: {banking_info["phone_number"]}')

def see_ssn():
    if not save_ssn:
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_ssn_choices']:
            save_ssn()
        elif selection.lower() in error_handling_negative['dont_save_ssn_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        ssn_info = save_ssn()
        print('Saved Social Security Number:')
        for ssn_info in save_ssn.items():
            print(f'Social Security Number: {ssn_info["ssn"]}')
            
def see_phone_number():
    if not save_phone_number():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_phone_number_choices']:
            save_phone_number()
        elif selection.lower() in error_handling_negative['dont_save_phone_number_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        phone_number_info = save_phone_number()
        print('Saved Phone Number')
        for phone_number, phone_number_info in save_phone_number.items():
            print(f'Phone Number: {phone_number_info["phone"]}, Primary Contact: {phone_number_info["primary"]}, Emergency Contact {phone_number_info["emergency"]}')
            
def see_login():
    if not save_login():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_login_choices']:
            save_login()
        elif selection.lower() in error_handling_negative['dont_save_login_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        login_info = save_login()
        print('Save Login')
        for login_info in save_login.items():
            print(f'Domain: {login_info["domain"]}, Username: {login_info["username"]}, Password: {login_info["password"]}, Email: {login_info["email"]}, Type: {login_info["account Type"]}, Name: {login_info["name"]}')
        
def see_email():
    if not save_email():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_email_choices']:
            save_email()
        elif selection.lower() in error_handling_negative['dont_save_email_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        email_info = save_email()
        print('Save Email')     
        for email_info in save_email.itmes():
            print(f'Email: {email_info["email"]}, Primary Email: {email_info["primary"]}, Business Email: {email_info["business"]}, Preffered Email for Communication: {email_info["preferred"]}')
            
def see_password():
    if not save_password():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_password_choices']:
            save_password()
        elif selection.lower() in error_handling_negative['dont_save_password_choice']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        password_info = save_password()
        print('Save Password')
        for password_info in save_password.items():
            print(f'Password: {password_info["password"]}')
            
def see_birth():
    if not save_birth():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save your data?: ').lower()
        if selection.lower() in error_handling_positive['save_birth_choices']:
            save_birth()
        elif selection.lower() in error_handling_negative['dont_save_birth_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else: 
            print('Invalid Input')
    else:
        birth_info = save_birth()
        print('Save Birthday')
        for birth_info in save_birth.items():
            print(f'Day: {birth_info["day"]}, Month: {birth_info["month"]}, Year: {birth_info["year"]}')
            
def see_gender():
    if not save_gender():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection.lower() in error_handling_positive['save_gender_choices']:
            save_gender()
        elif selection.lower() in error_handling_negative['dont_save_gender_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        print('Save Gender')
        for gender_info in save_gender.items():
            print(f'Sex: {gender_info["sex"]}, Gender: {gender_info["gender"]}, Pronouns: {email_info["pronouns"]}')
            
def see_nationality():
    if not save_nationality():
        selection = input('Uh Oh! There seems to be nothing save. Would you like to save something?: ').lower()
        if selection.lower() in error_handling_positive['save_nationality_choices']:
            save_nationality()
        elif selection.lower() in error_handling_negative['dont_save_nationality_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        nationality_info = save_nationality()
        print('Save Nationality')
        for nationality_info in save_nationality.items():
            print(f'Country: {nationality_info["nationality"]}, Country of Citizenship: {nationality_info["citizenship"]}, National Origin: {nationality_info["origin"]}')
            
def see_occupation():
    if not save_nationality():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_occupation_choices']:
            save_occupation()
        elif selection in error_handling_negative['dont_save_occupation_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        occupation_info = save_occupation()
        print('Save Occupation')
        for occupation_info in save_occupation.items():
            print(f'Job Title: {occupation_info["title"]}, Company: {occupation_info["company"]}, Profession: {occupation_info["profession"]}, Years of Experience: {occupation_info["years_of_experience"]}')
            
def see_education():
    if not save_education():
        selection = input('Uh Oh! There seems to be nothing save. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_education_choices']:
            save_education()
        elif selection in error_handling_negative['dont_save_education_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        education_info = save_education()
        print('Save Education')
        for education_info in save_education.info():
            print(f'highest level of education: {education_info["level"]}, Highest degree earned: {education_info["degree"]}, Field of study: {education_info["field"]}')
        
def see_medical():
    if not save_medical():
        selection = input('Uh Oh! There seemes to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_medical_choices']:
            save_medical()
        elif selection in error_handling_negative['dont_save_medical_choices']:
            choices = input('What would you like to do?: ').lower()
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        medical_info = save_medical()
        print('Save Medical')
        for medical_info in save_medical.items():
            print(f'Medical Condition {medical_info["condition"]}, Medical diagnosis {medical_info["diagnosis"]}, Name of Medication {medical_info}, Dosage of Medication {medical_info["name"]}, Allergies {medical_info["allergies"]}, Blood Type {medical_info["blood_type"]}, Chronic Illness {medical_info["illness"]}, Medical Devices or Impants {medical_info["implants"]}, Medical history {medical_info["history"]}')

def see_insurance():
    if not save_insurance():
        selection = input('Uh Oh! There seems to be nothing saved. would you like to save something?: ').lower()
        if selection in error_handling_positive['save_insurance_choices']:
            save_insurance()
        elif selection in error_handling_negative['dont_save_insurance_choices']:
            choices = input('What would you like to do?: ')
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        insurance_info = save_insurance()
        print('Save Insurance')
        for insurance_info in save_insurance.items():
            print(f'Insurance company name {insurance_info["name"]}, Insurance policy number{insurance_info["policy"]}, Insurance group number{insurance_info["group"]}, Insurance plan type{insurance_info["plan_type"]}, Insurance plan effective date{insurance_info["effective_date"]}, Insurance plan expiration date{insurance_info["expiration_date"]}, Insurance plan coverage details{insurance_info["details"]}, Assets Injured{insurance_info["insured"]}, Insurance plans deductible amount{insurance_info["deductibe"]}, Insurance plans co-pay amount{insurance_info["co_payment"]}')
       
def see_passport():
    if not save_passport():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ').lower()
        if selection in error_handling_positive['save_passport_choices']:
            save_passport()
        elif selection in error_handling_negative['dont_save_passport_choices']:
            choices = input('What would you like to do?: ')
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        passport_info = save_passport()
        print('Save Passport')
        for passport_info in save_passport.items():
            print(f'Passport number: {passport_info["passport"]}, Expiration date: {passport_info["expiration_date"]}')
            
def see_legal():
    if not save_legal():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ')
        if selection in error_handling_positive['save_legal_choices']:
            save_passport()
        elif selection in error_handling_negative['dont_save_legal_choices']:
            choices = input('What would you like to do?: ')
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        passport_info = save_passport()
        print('Save Passport')
        for passport_info in save_passport.items():
            print(f'Passport number: {passport_info["passport"]}, Expiration date: {passport_info["expiration_date"]}')
            
def see_ethnicity():
    if not save_ethnicity():
        selection = input('Uh Oh! There seems to be nothing saved. Would you like to save something?: ')
        if selection in error_handling_positive['save_ethnicity_choices']:
            save_passport()
        elif selection in error_handling_negative['dont_save_ethnicity_choices']:
            choices = input('What would you like to do?: ')
            if choices.lower() in user_choices:
                personal_information_selection()
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    else:
        passport_info = save_passport()
        print('Save Passport')
        for passport_info in save_passport.items():
            print(f'Passport number: {passport_info["passport"]}, Expiration date: {passport_info["expiration_date"]}')

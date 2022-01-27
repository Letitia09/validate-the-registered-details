#lex_auth_012694465248329728100

def validate_name(name):
    #Start writing your code here
    if name!=" " and len(name)<=15 and name.isalpha() :
        return True
    else:
        return False

def validate_phone_no(phno):
    #Start writing your code here
    if len(phno)==10 and phno.isdigit() and len(phno)!=phno.count(phno[0]):
        return True
    else:
        return False

def validate_email_id(email_id):
    #Start writing your code here
    l=['gmail','yahoo','hotmail']
    e=email_id.find('@')
    f=email_id.find('.com')
    if '@' in email_id and email_id.endswith('.com') and email_id[e+1:f] in l:
        return True
    else:
        return False

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    result1=validate_name(name)
    result2=validate_phone_no(phone_no)
    result3=validate_email_id(email_id)
    if result1==True:
        if result2==True:
            if result3==True:
                print("All the details are valid")
            else:
                print("Invalid email id")
        else:
            print("Invalid phone number")
    else:
        print("Invalid Name")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")

#OUTPUT : All the details are valid

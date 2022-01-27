# validate-the-registered-details
Write a python program to validate the details provided by a user as part of registering to a web application.<br>

Write a function validate_name(name) to validate the user name<br>
    Name should not be empty, name should not exceed 15 characters<br>
    Name should contain only alphabets<br>

Write a function validate_phone_no(phoneno) to validate the phone number<br>
    Phone number should have 10 digits<br>
    Phone number should not have any characters or special characters<br>
    All the digits of the phone number should not be same.<br>
    Example: 9999999999 is not a valid phone number<br>

Write a function validate_email_id(email_id) to validate email Id<br>
    It should contain one '@' character and '.com'<br>
    '.com' should be present at the end of the email id.<br>
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'<br>
Note: Consider the format of email id to be username@domain_name.com<br>

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.<br>

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.<br>

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.<br>


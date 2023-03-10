import bcrypt            #encryption module
import re                #special characters detection module
import os                #files module

from datetime import date, datetime        #date module

def date_function() :
    '''  takes User's date of birth 
         Parameters:
          year ==> should be between 1900 and 2022
          month ==> number of birth month => should be between 1 and 12
          day ==> number of birth day  => should be between 1 and 30
         returns:
          date of birth as [ year , month , day ] 
     '''
    flag = True                   #flag tells us if something wrong or not by setting it to True or False values
    
    #year input process
    while flag:

        #check if invalid year input
        try:
            year = int(input("Enter your birth year: "))

            #check if year is less than 1900 (invalid)
            if year < 1900 :
                print("No way! You are not that old")
                raise Exception()
            
            #check if year is greater than 2022 (invalid)
            if year > 2022 :
                print("No way! You can't be from the future!")
                raise Exception()
            
            #check if user age less than 4 years
            if 2022-int(year) < 5 :
                print("Of course you aren't a baby, try again with a valid year")
                raise Exception()
            flag = False
        except:
            print("invalid year! try again")
    #month input
    flag = True
    while flag:
        try:
            month = int(input("Enter your birth month (from 1 to 12): "))
            if month < 1 or month > 12 :
                print("No way! i told you, enter a number from 1 to 12")
                raise Exception()
            flag = False
        except:
            print("invalid month!")
    #day input
    flag = True
    while flag:
        try:
            day = int(input("Enter your birthday (from 1 to 30): "))
            if day < 1 or day > 30 :
                print("No way! i told you, enter a number from 1 to 30")
                raise Exception()
            flag = False
        except:
            print("invalid day!")
    return date(year, month, day)

#main function that we will export to main file
def registration() :
    ''' save  user information in database file 
        returns:
            message " registration completed! "
    '''
    #user information input process
    first_name = firstname()
    last_name = lastname()
    user = user_function()
    birth_date = date_function()
    email = email_function()
    password = password_function()

    #writing in database
    file =open("database.txt","a")                #append to file and if it's not exists create it
    space = ' '
    file.write(F"{first_name+space+last_name},{user},{birth_date},{email},{password},{2022-int(birth_date.year)}")     #every line in database should be in : first and last name, user name, birthdate, email, password, age
    file.write("\n")                              #making new line for the next registration
    file.close()
    print("registration completed!")

#user input process
def user_function():
    ''' takes username from user  
        Parameters:
         user ==> username 
                     must be in 6-30 characters 
                     can't contain special characters
                     First character can't be a number
                      not used by another user
        returns: username                
       '''
    #check if database file exists or not
    if if_file() : pass
    
    #username input process
    while 1 :
        file =open("database.txt","r").read()
        user = input("Enter a username: ")
        
        #check if input is empty
        if len(user) == 0 :
            print("you didn't type anything, please try again!")
            continue

        #check if username exists in database or not
        if user_exist(user) == False:
            print("Username taken! please try another username")
            continue

        #check if input has special characters
        if (bool(re.search('^[a-zA-Z0-9]*$',user))==False):
            print("username can't contain special characters")
            continue
        
        if user[0].isdigit() :
            print("First character in username can't be a number")
            continue

        #check if username less than 6 characters or greater than 30 characters (invalid)
        if len(user) < 6 or len(user) > 30 :
            print("Username must be in 6-30 characters, try again!")
            continue
        else:
               break
    return user

#user input and encrypting process
def password_function() :
    ''' takes password from user and Ask him to confirm the password and encode password so we can encrypt it
        then  decode it again to avoid encoding twice
        Parameters:
          password == password_confirmation
                                must be in 6-55 characters
        returns: password
    '''
    #password input process
    while 1 :
        password =input("enter a password: ")
        password_confirmation = input("Enter the password again: ")          #confirmation of password

        #check if input is empty
        if len(password) == 0 :
            print("you didn't type anything, please try again!")
            continue
        
        if len(password) < 6 :
            print("Password too short, try another one!")
            continue

        if len(password) > 55 :
            print("Password too long, try another one!")
            continue

        #confirmation check
        if password_confirmation == password :
            break
        else :
            print("Password not match! try again")
            continue
    password = password.encode('utf-8')                        #encoding password so we can encrypt it
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))       #encrypting password
    hashed = hashed.decode('utf8')                             #decode it again to avoid encoding twice
    return hashed

#email input process
def email_function() :
    ''' takes email from user and check if it already registered or not by email_exist() function
        Parameters: 
            email ==> user's email 
                    must contain '.' and '@'
        returns: email            
      '''
    #check if database file exists or not
    if if_file() : pass
    
    #email input process
    while 1 :
        file =open("database.txt","r").read()
        email = str(input("enter your email: "))

        #check if input is empty
        if len(email) == 0 :
            print("you didn't type anything, please try again!")
            continue
        
        #check if input is not an email (invalid)
        if '.' and '@' not in email :
            print("Invalid email! please try again")
            continue

        dot_flag = '.' in email
        if not dot_flag :
            print("Invalid email! please try again")
            continue
        
        #check if username exists in database or not
        if email_exist(email) == False:
            print("email already registered! please try another one")
            continue
        else :
            break
    return email

#function to check if user in database or not
def user_exist(user_to_check) :
  ''' chick if user taken by another user or not

      return:
        false ==> if username is taken befor
        true  ==> if username isn't taken befor
  '''
  #creating a dictionary for usernames from database
  dictionary = {}

  #check if database file exists or not
  if if_file() : pass
        
  file =open("database.txt","r")
  count = 0                        #to mark usernames numbers

  #filling of dictionary
  for line in file:
      x = line.split(",")
      user=x[1]
      dictionary["user",count] = user
      count = count + 1

  #check if username exists in dictionary (database) or not
  for key, value in dictionary.items():
    if str(user_to_check) == str(value):
        return False
  return True

#function to check if user in database or not
def email_exist(email_to_check) :
  '''  chick if email  already registered 

      return:
        false ==> if email is used befor
        true  ==> if email isn't used befor
  '''
  #creating a dictionary for usernames from database
  dictionary = {}

  #check if database file exists or not
  if if_file() : pass
        
  file =open("database.txt","r")
  count = 0                        #to mark usernames numbers

  #filling of dictionary
  for line in file:
      x = line.split(",")
      email=x[3]
      dictionary["email",count] = email
      count = count + 1

  #check if username exists in dictionary (database) or not
  for key, value in dictionary.items():
    if str(email_to_check) == str(value):
        return False
  return True

#first name input process
def firstname():
    ''' Takes the user's first name 
        Parameters:
            name1 ==> first name
                 can't contain special characters
                 can't contain numbers
        return: first name         
    '''
    #first name input process
    while 1:
        name1 =input("enter your first name: ")

        #check if input is empty
        if len(name1)==0:
            print("first name can't be empty!")
            continue

        #check if input has special characters
        if (bool(re.search('^[a-zA-Z0-9]*$',name1))==False):
            print("first name can't contain special characters")
            continue

        #check if input has numbers
        elif any(char.isdigit() for char in name1) :
            print("first name can't contain numbers")
            continue
        else:
            break
    return name1

#first name input process
def lastname():
    ''' Takes the user's last name 
        Parameters:
            name1 ==> last name
                 can't contain special characters
                 can't contain numbers
        return: last name         
    '''
    #last name input process
    while 1:
        name2 =input("enter your last name: ")

        #check if input is empty
        if len(name2)==0:
            print("last name can't be empty!")
            continue

        #check if input has special characters
        if (bool(re.search('^[a-zA-Z0-9]*$',name2))==False):
            print("last name can't contain special characters")
            continue

        #check if input has numbers
        elif any(char.isdigit() for char in name2) :
            print("last name can't contain numbers")
            continue
        else:
            break
    return name2

#function to check if database file exists or not
def if_file() :
    ''' check if database file exists or not 
        if not ask the user to enter 't'  to try again  or press any key to  end the program
        returns:
            true ==> if database file exists
            continues to the next iteration ==>  if user enter 't'
            end the program ==> if user press any key
     '''
    while 1 :
        if os.path.isfile('./database.txt') :
            return True
        else :
            x = input("database file not exists, to try again type 't', to end the program press any key! : ")
        if x == 't' :
            continue
        else :
            quit()
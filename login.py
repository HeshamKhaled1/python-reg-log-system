import bcrypt                   #encryption module
import os                       #files module

#main function that we will export to main file
def login():
    ''' takes username or email from user and check if it exists in database or not by user_exist() and email_exist() functions
        and takes password from user check if password right or not by password_exist()
        returns:
          message " Welcome! " ==> if username or email and password are true
          message " Invaled user name or password,try again " then continues to the next iteration ==> if username or email and password are not true
    ''' 
    while True :
        username_or_email = input("enter your username or email: ")

        #check if database file exists or not
        if if_file() : pass
        
        file =open("database.txt","r").read()

        #check if username of password exists in database or not
        is_user = user_exist(username_or_email) or email_exist(username_or_email)

        #password input
        password =input("enter the password: ")

        #check if password right or not(exists in database or not)
        is_password = password_exist(password)
        if is_user and is_password :
          print("Welcome!")
          break
        else:
          print("Invaled user name or password,try again")
          continue

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
    if value == user_to_check:
        return True
  return False

#function to check if password in database or not
def password_exist(password_check) :
  '''     check if password exists in database file or not
          return:
        true ==> if password exists in database file
        false  ==> if not
 '''  
  #creating a dictionary for usernames from database
  dictionary = {}

  #check if database file exists or not
  if if_file() : pass

  file =open("database.txt","r")
  count = 0                             #to mark passwords numbers

  #filling of dictionary
  for line in file:
        x = line.split(",")
        hashed = x[4]
        dictionary["password",count] = hashed
        count = count + 1

    #check if password exists in dictionary (database) or not
  for key, value in dictionary.items():
        hashed = str(hashed)                            #make the hashed password string not bytes
        hashed = hashed.encode('utf-8')                 #encode it again
        check = str(password_check)                     #make sure that the password entered from user is string
        check = check.encode('utf-8')                   #encode it

        #use try and except to avoid any errors in salt
        try :
          if bcrypt.checkpw(check, hashed):             #to use this function we must encode two operands we want to compare and that we did above
              return True
          else:
              return False
        except :
          print("")

#function to check if email in database or not
def email_exist(email_to_check) :
  
  #creating a dictionary for usernames from database
  dictionary = {}
  ''' takes email from user and check if it already registered  or not by email_exist() function
        Parameters: 
            email ==> user's email 
                    must contain '.' and '@'
        returns: email            
      '''

  #check if database file exists or not
  if if_file() : pass

  file =open("database.txt","r")
  count = 0
  for line in file:
        x = line.split(",")
        user=x[3]
        dictionary["user",count] = user
        count = count + 1

  for key, value in dictionary.items():
      if value == email_to_check:
          return True
  return False

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
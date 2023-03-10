from registeration import *               #importing all functions in registration file
from login import *                       #importing all functions in login file

#registration or login process
while 1:

     #check if user want to login or register
     reg_login = input("Do you want to register(reg) or login(log)? : ")

     #if user want to register so we call registration function (from registration file)
     if(reg_login == "reg"):
       registration()
       break

     #if user want to login so we call login function (from login file)
     elif(reg_login == "log"): 
         login()
         break
     
     #check if user entered wrong data (not "reg" or "log")
     else:
         print("Error!!\nwrite reg or log")  
         continue
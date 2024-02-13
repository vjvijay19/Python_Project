import os
from pymongo.mongo_client import MongoClient
from find_a_doctor import find_a_doctor
from appointment import appointment
from cancel_appointment import cancel_appointment
from about_project import about_project

db_uri = "mongodb+srv://jvijay1901:Vj$191101@cluster0.4oypqox.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_uri)
db = client["health_project"]


print("""
         
░█████╗░░█████╗░  ██╗░░░░░██╗███████╗███████╗  ░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗  ██║░░░░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║███████║  ██║░░░░░██║█████╗░░█████╗░░  ██║░░╚═╝███████║██████╔╝█████╗░░
██║░░██║██╔══██║  ██║░░░░░██║██╔══╝░░██╔══╝░░  ██║░░██╗██╔══██║██╔══██╗██╔══╝░░
╚█████╔╝██║░░██║  ███████╗██║██║░░░░░███████╗  ╚█████╔╝██║░░██║██║░░██║███████╗
░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝╚═╝░░░░░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝""")
print()
print()
print()
print()
print(input("PRESS ANY KEY TO CONTINUE..."))
os.system("cls")
print("""      
                                                
                                
                       
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀█ ▄▀█   █░░ █ █▀▀ █▀▀   █▀▀ ▄▀█ █▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄█ █▀█   █▄▄ █ █▀░ ██▄   █▄▄ █▀█ █▀▄ ██▄
      
                                    
                                        ██╗
                                      ██████╗
                                      ╚═██╔═╝
                                        ╚═╝                           
                                      
                                         
                                      
                                                                    
                            
       """)
print()
print(input("PRESS ANY KEY TO VIEW INFORMATIONS..."))

while True:

  print("MENU")
  print("""
  1. Find a Doctor
  2. Book Appointment
  3. Cancel Appointment
  4. About Project
  5. Exit
  """)

  a = int(input("Choose an option:"))

  if a == 1:
      
      find_a_doctor(db)
      input()
      os.system("cls")

  if a == 2:
      
      appointment(db)
      input()
      os.system("cls")

  if a == 3:
       
       cancel_appointment(db)
       input()
       os.system("cls")

  if a == 4:
     
     about_project(db)
     input()
     os.system("cls")    
     
  if a == 5:
     break  





   

       
       

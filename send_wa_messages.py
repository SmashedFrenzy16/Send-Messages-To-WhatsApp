import pywhatkit
import sys


closing = False

ques = input("Welcome to the WhatsApp messaging Python file! Do you want to send a message to a provate chat (p) or a group (g)?: ")

mess = input("Type in the message you want to send: ")

hr = int(input("Enter the hour you want to send it at (00 - 24 - 2 digit number format please): "))

mn = int(input("Enter the minute you want to send the message at (00 - 60 - 2 digit number format please): "))

askclose = input("Do you want to close WhatsApp after sending message? (y/n): ")

if askclose == "y" or askclose == "Y":
  
  closing = True
  
  closedur = float(input("Enter the closing amount duration: "))
  
  if ques == "p":
  
  pywhatkit.sendwhatmsg("<Enter Phone Number Here>", mess, hr, mn, closing, closedur)
  
  elif ques == "g":
    
    pywhatkit.sendwhatmsg_to_group("<Enter Group ID Here>", mess, hr, mn, closing, closedur)
    
  else:
    
    print("Sorry, that input was not recognized. Program now terminating.")
    
    sys.exit()
  
else:
  
  closing = False


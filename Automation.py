
"""
A basic AI script that automatically replies to emails based on simple keywords in the message.
💬 Example Input (email content):
“I need help with my order.
“Can you tell me about your refund policy?”
“Thanks for the support!”

⚙️ Automation Logic:
If the message contains the word "order", reply: "We’re happy to help with your order. Our team will contact you soon."
If it contains "refund", reply: "Here is our refund policy link..."
If none of those, reply: "Thank you for reaching out. We'll get back to you shortly."
"""

print("Enter you message: ")
message = input()
if "order" in message:
    print("our team ready to recieve your order....")

if "refund" in message:
    print("here some refund for you...")

if "help" in message:
    print("our team is ready for help....")


#training A simple AI model:
def num (number):
    if number % 2 == 0:
        print("number is even ")
    else:
        print("number is odd")
num(9)


#Rename multiple file automatically
import os
file = ["shumial","ali","aslam","rehan"]

for file in file:
    newfile = "hello"" " + file
    print(newfile)


#create email of names in email:
student = ["Shumail Saman","ali","rehan ali","karam","Sami"]

for student in student:
    email = student.lower().replace(" ","")+ "iac@gmail.com"
    print(email)


"""
You are designing a system that needs to simulate data collection from a sensor that gives a reading every second for 5 seconds.
Logic:
Collect and print the message: "Reading sensor data..." 5 times.
"""

print("Enter data:")
data = input()
for n in range(5):
         print(data)


#Timmer:

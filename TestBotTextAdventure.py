import time
x = input("???: Hi there List your family")
family = x.split()
Ted = False
for x in family:
    if (x) == ("testbot") or x == ("TestBot"):
        Ted = True
if len(family) >1:
        print("???: Oh,That's Nice.")
if Ted == True:
    time.sleep(1.5)
    print("TestBot: Wait, TestBot is MY name!!!")
else:
   time.sleep(1.5)
   print("TestBot: My name is TestBot")
time.sleep(1.5)
y = input ("TestBot: What is yours?")
time.sleep(1.5)
z = input ("TestBot: Nice to meet you "+y+", what is your hobby?")
time.sleep(.6)
print("TestBot: nice")
time.sleep(1.3)
print("TestBot: ...")
time.sleep(2)
print("TestBot: So what now?")
time.sleep(1.5)
r = input("TestBot: Ooh I know, How about I tell you a riddle (reply with \"sure\" if you want to hear a riddle, reply with \"no\" if you do not want to hear a riddle)")
if r == ("sure"):
    a = input("What is")





    
    
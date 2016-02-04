import Skype4Py
import sys
import random
import time
    

skype = Skype4Py.Skype()
skype.Attach()
print("Attached: user is " + skype.CurrentUser.FullName)


        
def commands(Message, Status):
    if Status == 'SENT' or Status == 'RECEIVED':
        if Message.Body[0] == "!":
            command = Message.Body
            if(Message.Body == "!wordgame"):
                commands[command](Message,Status)
            commands[command](Message)
                
    else:
        pass
#more

skype.OnMessageStatus = commands;

def commandChristmas(Message):
    Message.Chat.SendMessage("..........(*)....")
    Message.Chat.SendMessage("...........^......")
    Message.Chat.SendMessage("........../.\.....")
    Message.Chat.SendMessage("......../.....\...")
    Message.Chat.SendMessage("....../_____\.")
    Message.Chat.SendMessage("............|..")


def commandHelp(Message):
    Message.Chat.SendMessage("AsciiBot: brings art to skype.")
    Message.Chat.SendMessage("AsciiBot: Type '!commands' for a list of commands")

def commandList(Message):
    Message.Chat.SendMessage("'!help': help command")
    Message.Chat.SendMessage("'!christmas' : decoration")
    Message.Chat.SendMessage("'!halloween': decoration")
    Message.Chat.SendMessage("'!rr': russian roulette")
    
def russianroullete(Message): #needs to be softcoded
    members = Message.Chat.Members
    alive = Message.Chat.Members
    Message.Chat.SendMessage("AsciiBot: Starting Russian Roullette")
    
    
    r2 = random.randint(0,10) #change number for number of contacts in group,
    tester = members[r2]#ALSO AFFECTS CHANCE DONT GO OVER 6
    while(alive.count > 0):
        r1 = random.randint(0,10)#change number for number of contacts in group
        chosen = alive[r1]
        Message.Chat.SendMessage("The Gun points at: " + chosen.FullName)
        time.sleep(1)
        Message.Chat.SendMessage("3")
        time.sleep(1)
        Message.Chat.SendMessage("2")
        time.sleep(1)
        Message.Chat.SendMessage("1")
        time.sleep(1)
        if(chosen == tester):
            Message.Chat.SendMessage("POW, the gun leaves a deadly hole in " + tester.FullName)
            break
        else:
            response = random.randint(0,2)
            if(response ==0):
                Message.Chat.SendMessage("click, the gun was empty")
            if(response ==1):
                Message.Chat.SendMessage("BOOM, a shower of confetti is sprayed over you")
            if(response ==2):
                Message.Chat.SendMessage("PAPAA, an Italian flag pops out of the barrel of the gun. Viva la italia!")                     
                    
def Halloween(Message):
    Message.Chat.SendMessage("..........-...........")
    Message.Chat.SendMessage("..........)\...........")
    Message.Chat.SendMessage("....--'`--`'--.....")
    Message.Chat.SendMessage("./...^.....^...\..")
    Message.Chat.SendMessage(".\..\/\/\/\/../..")
    Message.Chat.SendMessage("..'----------'....")

def Wordgame(Message,Status):
    Message.Chat.SendMessage("AsciiBot: Wordgame! say a word that starts with the last letter of the previous word")                      
    Message.Chat.SendMessage("AsciiBot: MAKE SURE YOUR SUBMISSION BEGINS WITH #")
    members = Message.Chat.Members
    lastletter = "r"
    i=0

    
    chosen = members[i]
    j = random.randint(0,3)
    randtopic = topic[j]
    Message.Chat.SendMessage("The topic is: " + randtopic)
    Message.Chat.SendMessage("Ok, " + chosen.FullName + " your word please, end with: r")
    
    if Status == 'SENT' or Status == 'RECEIVED':
       if Message.Body[0] == "#":
          word = Message.Body
          lastletter2 = word[-1:]
          if(word == "!end"):
             exit()
          ++i 
          if(lastletter2 == lastletter):
             lastletter = lastletter2
             Message.Chat.SendMessage("Good Job~")
          else:
             Message.Chat.SendMessage("NOPE, " + chosen.FullName + " is the loser")
             
            
    
commands = {
        '!christmas' : commandChristmas,
        '!help' : commandHelp,
        '!rr' : russianroullete,
        '!halloween' : Halloween,
        '!commands': commandList,
        '!wordgame' : Wordgame
    }
topic = ["animals","food","places","runescape"]

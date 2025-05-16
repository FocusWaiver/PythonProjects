# GameScoreboard.py
# To provide round calculations for keeping score
#  5/14/25 - fw
#
#

#path for files
path = "UPDATE"
#import os

def FileError(playfile):
    #Can this be the file name?
    symbols = "{}|[]!@#$%^&*()-_=+;:?.,<>"
    for sym in symbols:
        symfind = playfile.find(sym)
        if symfind >= 0:
            print("Sorry, there are invalid characters in your filename. Try again")
            return True
    #Does this file already exist?
    #exist = os.path.exists(playfilefull)
    exist = False
    if exist:
        print("Sorry, that file name already exists.")
        return True
    else:
        print("Saving...")
        return False
        
def newGame():
    roundzero = []
    print("Who is playing?")
    players = input()
    playlist = players.split(",")
    #File name
    print("What would you like to name this file?")
    playfile = input()
    playfiletxt = playfile+".txt"
    mistakes = FileError(playfile)
    if mistakes:
        playfile = input()
    #create new file with name
    #open path+playfiletxt
    #write playlist to file
    for each in playlist:
        entry = each+"-0"
        roundzero.append(entry)
    #upload roundzero
    print("Great, your save file is called ", playfiletxt)
    print("Have Fun!")
    
def contGame():
    #!
    #change this for less typing between rounds
    contfilename = "game.txt"
    #!
    
    #testing list
    content = ("n,k,m","['n-0','k-0','m-0']","['n-2','k-6','m-1']","['n-22','k-46','m-10']")
    updatelist = []
    #contf = open(game.txt)
    #content = contf.readlines()
    playerlist = content[0]
    playsplit = playerlist.split(",")
    currentscore = content[-1]
    #make a function to use multiple times?
    junk = ["[","]","'"]
    for j in junk:
        currentscore = currentscore.replace(j,"")
    print(currentscore)
    currsplit = currentscore.split(",")
    for i in currsplit:
        separate = i.split("-")
        player = separate[0]
        score = int(separate[1])
        print("what was ",player, "'s score this round?")
        newscore = input()
        #try int
        newint = int(newscore)
        addition = str(score+newint)
        updatelist.append(player+"-"+addition)
    print("The scores for round ", len(content)-1, "are", updatelist)
    #upload
        
    
    
# Welcome
print("Welcome!")
#New or continuing game
print("0 for a new game, 1 to continue a past game")
#gameAns = input()
gameAns = "1"
if gameAns == "0":
    newGame()
elif gameAns == "1":
    contGame()
else:
    print("Sorry, invalid input.")

#pickup a different saved game? Can python print folder contents?

# GameScoreboard.py
# To provide round calculations for keeping score
#  5/14/25 - fw
#
# README
# Two hard code sections that need to be edited.
# (1) Find path of directory you wish new game save files to be stored
# (2) Update desired game file after creating a new save to avoid having to type in...
# desired save file name between every round.
#
#

#path for files, Edit (1)
path = "/storage/emulated/0/Documents/Pydroid3/mobilePython/"
import os
#Can use the following command to find current working directory
#print(os.getcwd())

#used to remove storage artifacts from saved strings
def dejunk(dirty):
    junk = ["[","]","'","(",")"," "]
    for j in junk:
    	clean = dirty.replace(j,"")
    	dirty = clean
    return clean
	
#Verifying name of save file input by user is valid/does not already exist
def FileError(playfile):
    symbols = "{}|[]!@#$%^&*()-_=+;:?.,<>"
    for sym in symbols:
        symfind = playfile.find(sym)
        if symfind >= 0:
            print("Sorry, there are invalid characters in your filename. Try again")
            return True
    #Does this file already exist?
    exist = os.path.exists(playfile)
    #exist = False
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
    #File name input by user
    print("What would you like to name this file?")
    playfile = input()
    playfiletxt = playfile+".txt"
    mistakes = FileError(playfile)
    if mistakes:
        playfile = input()
    #create new file with input name
    playf= open(path+playfiletxt, "x")
    playf.close()
    #write playlist to file
    for each in playlist:
        entry = each+"-0"
        roundzero.append(entry)
    #upload roundzero for consistancy in contGame() data retrieval
    playrz = open(path+playfiletxt, "w")
    playrz.write(str(playlist)+"\n")
    playrz.write(str(roundzero))
    playrz.close()
    print("Great, your save file is called ", playfiletxt)
    print("Have Fun!")
    
def contGame():
    #!
    #change this for less typing between rounds, Edit (2)
    contfilename = "GinGame51925.txt"
    #!
    
    updatelist = []
    cplayerlist = []
    contf = open(contfilename,"r")
    contfsplit = contf.read()
    contf.close()
    content = contfsplit.split("\n")
    currentscorej = content[-1]
    currentscore = dejunk(currentscorej)
    currsplit = currentscore.split(",")
    for i in currsplit:
        separate = i.split("-")
        playerd = separate[0]
        playerc = dejunk(playerd)
        scorec = dejunk(separate[1])
        score = int(scorec)
        print("what was ",playerc, "'s score this round?")
        newscore = input()
        #Convert stored score from string to integer for calculations
        #!INPUT TRY for Errors!
        newint = int(newscore)
        addition = str(score+newint)
        updatelist.append(playerc+"-"+addition)
    print("The scores for round ", len(content)-1, "are", updatelist)
    #upload latest score to save file
    roundf = open(contfilename,"a")
    roundf.write("\n"+str(updatelist))
    roundf.close()
        
    
    
# Initial interface/Welcome
print("Welcome!")
#New or continuing game
print("0 for a new game, 1 to continue a past game")
gameAns = input()
if gameAns == "0":
    newGame()
elif gameAns == "1":
    contGame()
else:
    print("Sorry, invalid input.")
    
#TODO
# Add Try for score input




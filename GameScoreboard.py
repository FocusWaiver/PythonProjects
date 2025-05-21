# GameScoreboard.py
# To provide round calculations for keeping score
#  5/14/25 - fw
#
#

#path for files
path = "/storage/emulated/0/Documents/Pydroid3/mobilePython/"
import os
#print(os.getcwd())

def dejunk(dirty):
    junk = ["[","]","'","(",")"," "]
    for j in junk:
    	clean = dirty.replace(j,"")
    	dirty = clean
    return clean
	

def FileError(playfile):
    #Can this be the file name?
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
    #File name
    print("What would you like to name this file?")
    playfile = input()
    playfiletxt = playfile+".txt"
    mistakes = FileError(playfile)
    if mistakes:
        playfile = input()
    #create new file with name
    playf= open(path+playfiletxt, "x")
    playf.close()
    #write playlist to file
    for each in playlist:
        entry = each+"-0"
        roundzero.append(entry)
    #upload roundzero
    playrz = open(path+playfiletxt, "w")
    playrz.write(str(playlist)+"\n")
    playrz.write(str(roundzero))
    playrz.close()
    print("Great, your save file is called ", playfiletxt)
    print("Have Fun!")
    
def contGame():
    #!
    #change this for less typing between rounds
    contfilename = "GinGame51925https://youtu.be/K5KVEU3aaeQ?si=r2ifwliXevGaMVBV.txt"
    #!
    
    #testing list
    #content = ("n,k,m","['n-0','k-0','m-0']","['n-2','k-6','m-1']","['n-22','k-46','m-10']")
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
        #try int
        newint = int(newscore)
        addition = str(score+newint)
        updatelist.append(playerc+"-"+addition)
    print("The scores for round ", len(content)-1, "are", updatelist)
    #upload
    roundf = open(contfilename,"a")
    roundf.write("\n"+str(updatelist))
    roundf.close()
        
    
    
# Welcome
print("Welcome!")
#New or continuing game
print("0 for a new game, 1 to continue a past game")
gameAns = input()
#gameAns = "3"
if gameAns == "0":
    newGame()
elif gameAns == "1":
    contGame()
else:
    print("Sorry, invalid input.")

#pickup a different saved game? Can python print folder contents?


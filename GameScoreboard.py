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
    print("Who is playing?")
    players = input()
    playlist = players.split(",")
    #File name
    print("What would you like to name this file?")
    playfile = input()
    playfilefull = path+playfile+".txt"
    mistakes = FileError(playfile)
    if mistakes:
        playfile = input()
    #create new file with user name
    #write playlist to file
    print("Great, your save file is called ", playfilefull)
    print("Have Fun!")
    
    
# Welcome
print("Welcome!")
#New or continuing game
print("0 for a new game, 1 to continue a past game")
#gameAns = input()
gameAns = "0"
if gameAns == "0":
    newGame()
    
    
elif gameAns == "1":
    print(1)
else:
    print("Sorry, invalid input.")
#Grab cache file with information

# If new, Prompt for team/player names
#prompt name of file save
#will need try() and loop to check name won’t break anything
#store information/write to cache or make new file? Format it so you can look back

#if continue, split teams/player to retrieve scores, Count /n for round number
#print game information, active score, round number
#prompt iteration of score entry
#calculate new score
#return updated score
#save new information

#pickup a different saved game? Can python print folder contents?





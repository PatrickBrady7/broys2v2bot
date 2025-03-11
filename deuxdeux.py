import csv

#Use sheets in excel to differentiate between tournaments?
#Have a master sheet that pulls data from all other sheets as like a lifetime stats?
#give user option with stats to look at lifetime vs a specific event?
#***Add stats leaders to eventStats()

stats = open('2v2stats.csv', 'r')

def HSpercentage(player):
    for row in stats: 
        entries = row.split(",")
        if entries[0] == player:
            print("HS%: " + entries[13])

def ADR(player):
    for row in stats: 
        entries = row.split(",")
        if entries[0] == player:
            print("ADR: " + entries[14])

def KPR(player):
    for row in stats:
        entries = row.split(",")
        if entries[0] == player: 
            print("KPR: " + entries[8])   
  
def DPR(player):
    for row in stats:
        entries = row.split(",")
        if entries[0] == player:
            print("DPR: " + entries[9])   

def EFR(player):
    for row in stats:
        entries = row.split(",")
        if entries[0] == player:
            print("EF per Round: " + entries[11])  

def UDR(player):
    for row in stats:
        entries = row.split(",") 
        if entries[0] == player:
            print("UD per Round: " + entries[10])  

def KD(player):
    for row in stats:
        entries = row.split(",") 
        if entries[0] == player:
            return entries[12]

def Rounds(player):
    for row in stats:
        entries = row.split(",") 
        if entries[0] == player:
            return entries[7]
              

def playerStats(player):
    print("Rounds played:" + str(Rounds(player)))
    print("KD: ", end = "")
    print(KD(player))
    ADR(player)
    print("\t")
    HSpercentage(player)
    print()
    KPR(player)
    print("\t")
    DPR(player)
    print()
    UDR(player)
    print("\t")
    EFR(player)
    print()
    #print("'!advStats *player*' for advanced stats")

def eventStats(tournamnet):
    winners = []
    EVPs = [] #List for EVPs
    MVP = ""
    print("Summary fo stats for " + tournamnet + ":\n") #Grab from sheet name?
    #Iterate to find mvp/evp/placements
    for row in stats:
        entries = row.split(",")
        name = entries[0] 
        for column in entries:
            if column == "MVP: ": 
                MVP = name
            elif column == "EVP: ":
                EVPs.append(name)
            elif column == "1st":
                winners.append(name)

                
    print("Winners: " + winners + "\n")
    print("MVP: " + MVP + "\n")
    print("EVPs: " + EVPs + "\n")
    #show stats leaders for the tourney?

#print(Rounds("Joey"))
#print(KD("Joey"))
#print(Rounds("Danzo"))
#print(Rounds("Joey"))

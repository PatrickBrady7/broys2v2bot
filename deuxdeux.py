import csv

#Master excel sheet with lifetime page, other sheets are specific tournaments
#This can then be saved as multiple csv files, which can be used to gather stats for an event
#Master sheet will be lifetime stats, other sheets will be labeled by event

#give user option with stats to look at lifetime vs a specific event?

#Add stats leaders to eventStats()

#***need to put all spreadsheet data into a nested list to parse or continuously open and close file >:)

stats = open('2v2stats.csv', 'r')
nest = []
for name in stats:          #Puts all data in a nested list for easier & quicker access
    rows = name.split(",")
    nest.append(rows)
stats.close()

def HSpercentage(player):
    for row in nest:
        if row[0] == player:
            print("HS%: " + row[13] + "%")

def ADR(player):
    for row in nest: 
        if row[0] == player:
            print("ADR: " + row[14], end = "\t\t")

def KPR(player):
    for row in nest:
        if row[0] == player: 
            print("KPR: " + row[8], end = "\t")   
  
def DPR(player):
    for row in nest:
        if row[0] == player:
            print("DPR: " + row[9])   

def EFR(player):
    for row in nest:
        if row[0] == player:
            print("EF per Round: " + row[11])  

def UDR(player):
    for row in nest:
        if row[0] == player:
            print("UD per Round: " + row[10], end = "\t\t")  

def KD(player):
    for row in nest:
        if row[0] == player:
            print("KD: " + row[12], end = "\t")
            return row[12]

def Rounds(player):
    for row in nest:
        if row[0] == player:
            return row[7]
              

def playerStats(player):
    print(player + "'s stats over " + str(Rounds(player)) + "rounds played:")
   
    KD(player)
    ADR(player)
    HSpercentage(player)

    KPR(player)
    DPR(player)

    UDR(player)
    EFR(player)

def eventStats(tournamnet):
    winners = []
    EVPs = [] #Lists for EVPs & winners
    MVP = ""
    print("Summary fo stats for " + tournamnet + ":\n") #Grab from sheet name?
    #Iterate to find mvp/evp/placements
    for row in nest:
        name = row[0] 
        for column in row:
            if column == "MVP": 
                MVP = name
            elif column == "EVP":
                EVPs.append(name)
            elif column == "1st":
                winners.append(name)

                
    print("Winners: " + winners + "\n")
    print("MVP: " + MVP + "\n")
    print("EVPs: " + EVPs + "\n")
    #show stats leaders for the tourney?
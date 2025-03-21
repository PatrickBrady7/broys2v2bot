import csv
#Add stats leaders to eventStats()

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
            print("ADR: " + row[14], end = "\t")

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
            print("EFR: " + row[11])  

def UDR(player):
    for row in nest:
        if row[0] == player:
            print("UDR: " + row[10], end = "\t")  

def KD(player):
    for row in nest:
        if row[0] == player:
            print("KD: " + row[12], end = "\t\t")
            return row[12]

def Rounds(player):
    for row in nest:
        if row[0] == player:
            return row[7]
              

def playerStats(player):
    print(player + "'s stats over " + str(Rounds(player)) + " rounds played:")
   
    KD(player)
    ADR(player)
    HSpercentage(player)

    KPR(player)
    DPR(player)

    UDR(player)
    EFR(player)

def eventStats():
    winners = []
    EVPs = [] #Lists for EVPs & winners
    MVP = ""
    print("Summary of stats for Broys Wingman Tourney:")
    print()
    #Iterate to find mvp/evp/placements
    for row in nest:
        name = row[0]

        if row[16] == "MVP\n": 
            MVP = name
        if row[16] == "EVP\n":
            EVPs.append(name)
        if row[15] == "1st":
            winners.append(name)

                
    print("Winners: " + winners[0] + " & " + winners[1])
    print()
    print("MVP: " + MVP)
    playerStats(MVP)
    print()
    print("EVPs:" , end =" ")

    for index in EVPs:
        if index == EVPs[-1]:
            print("& " + index)
        else:
            print(index, end = ", ")

eventStats()
#import pandas as pd

#Use sheets in excel to differentiate between tournaments?
#Have a master sheet that pulls data from all other sheets as like a lifetime stats?
#give user option with stats to look at lifetime vs a specific event?
#player object, pull params from other columns in excel after the name??
#***Add stats leadesr to eventStats()


#pd.read_excel("2v2stats.xlsx")
stats = open("2v2stats.xslx")

def HSpercentage(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            HSP = columnN

    print("HS%: " + HSP)

def ADR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            ADR = columnO  
    
    print("ADR: " + ADR)

def KPR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            KPR = columnI
    
    print("KPR: " + KPR)   
  
def DPR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            DPR = columnJ
    
    print("DPR: " + DPR)   

def EFR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            EFR = columnL
    
    print("EF per Round: " + EFR)  

def UDR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            UDR = columnK
    
    print("UD per Round: " + UDR)  

def KD(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            KD = columnM
    
    print("KD: " + KD)

def Rounds(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            R = columnH
    print(R)     

def playerStats(self, player):
    print(player + "'s stats over " + Rounds(self, player) + " rounds:\n")
    KD(self, player)
    print("\t")
    ADR(self, player)
    print("\t")
    HSpercentage(self, player)
    print()
    KPR(self, player)
    print("\t")
    DPR(self, player)
    print()
    UDR(self, player)
    print("\t")
    EFR(self, player)
    print()
    #print("'!advStats *player*' for advanced stats")

def eventStats(self, tournamnet):
    winners = []
    EVPs = [] #List for EVPs
    MVP = ""
    print("Summary fo stats for " + tournamnet + ":\n") #Grab from sheet name?
    #Iterate to find mvp/evp/placements
    for entry in stats:
        name = ""
        name = columnA 
        for column in entry:
            if column == "MVP": 
                MVP = name
            elif column == "EVP":
                EVPs.append(name)
            elif column == "1st":
                winners.append(name)

                
    print("Winners: " + winners + "\n") #column P
    print("MVP: " + MVP + "\n") #Column Q
    print("EVPs: " + EVPs + "\n")
    #show stats leaders for the tourney?


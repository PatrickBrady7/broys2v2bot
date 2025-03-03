#import pandas as pd
stats = open("2v2stats.xsl")

def HSpercentage(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            K = columB
            HS = columC

    print("HS%: " + K/HS)

def ADR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            ADR = columG  
    
    print("ADR: " + ADR)

def KPR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            K = columB
            R = columH
    
    print("KPR: " + K/R)   
  
def DPR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            D = columD
            R = columH
    
    print("DPR: " + D/R)   

def EFR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            EF = columF
            R = columH
    
    print("EF per Round: " + EF/R)  

def UDR(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            UD = columE
            R = columH
    
    print("UD per Round: " + UD/R)  

def KD(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            K = columB
            D = columD
    
    print("KD: " + K/D)

def Rounds(self, player):
    #separate by rows
    for entry in stats: 
        if entry == player.name:  #player input will determine row
            R = columH
    print(R)     

def playerStats(self, player):
    print(player + "'s stats over " + Rounds(self, player) + " rounds:\n")
    KD(self, player)
    print("\t")
    ADR(self, player)
    print("\t")
    HSpercentage(self, player)
    print("\n")
    KPR(self, player)
    print("\t")
    DPR(self, player)
    print("\n")
    UDR(self, player)
    print("\t")
    EFR(self, player)
    print("\n")
    #print("'!advStats *player*' for advanced stats")
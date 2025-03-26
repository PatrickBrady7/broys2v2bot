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
            return row[13]

def ADR(player):
    for row in nest: 
        if row[0] == player:
            return row[14]

def KPR(player):
    for row in nest:
        if row[0] == player: 
            return row[8]   
  
def DPR(player):
    for row in nest:
        if row[0] == player:
            return row[9]   

def EFR(player):
    for row in nest:
        if row[0] == player:
            return row[11]  

def UDR(player):
    for row in nest:
        if row[0] == player:
            return row[10]

def KD(player):
    for row in nest:
        if row[0] == player:
            return row[12]

def Rounds(player):
    for row in nest:
        if row[0] == player:
            return row[7]
              

def playerStats(player):
    print(player + "'s stats over " + str(Rounds(player)) + " rounds played:")
   
    print("KD: " + KD(player))
    print("ADR: " + ADR(player))
    print("HS%: " + HSpercentage(player))

    print("KPR: " + KPR(player))
    print("DPR: " + DPR(player))

    print("UDR: " + UDR(player))
    print("EFR: " + EFR(player))

def eventStats():
    winners = []
    EVPs = [] #Lists for EVPs & winners
    MVP = ""
    kdLeader, kdLeader2, kdLeader3= "0", "0", "0"
    kprLeader, kprLeader2, kprLeader3 = "0", "0", "0"
    adrLeader, adrLeader2, adrLeader3 = "0", "0", "0"
    hspLeader, hspLeader2, hspLeader3 = "0", "0", "0"
    dprLeader, dprLeader2, dprLeader3 = "1", "1", "1"
    udrLeader, udrLeader2, udrLeader3 = "0", "0", "0"
    efrLeader, efrLeader2, efrLeader3 = "0", "0", "0"
    kdLeaderName, kdLeaderName2, kdLeaderName3 = "", "", ""
    kprLeaderName, kprLeaderName2, kprLeaderName3 = "", "", ""
    adrLeaderName, adrLeaderName2, adrLeaderName3 = "", "", ""
    hspLeaderName, hspLeaderName2, hspLeaderName3 = "", "", ""
    dprLeaderName, dprLeaderName2, dprLeaderName3 = "", "", ""
    udrLeaderName, udrLeaderName2, udrLeaderName3 = "", "", ""
    efrLeaderName, efrLeaderName2, efrLeaderName3 = "", "", ""

    print("Summary of stats for Broys Wingman Tourney:")
    print()
    #Iterate to find event stats
    for row in nest:
        name = row[0]
        kdCurr, adrCurr, hspCurr = KD(name), ADR(name), HSpercentage(name)
        kprCurr, dprCurr = KPR(name), DPR(name)
        udrCurr, efrCurr = UDR(name), EFR(name)
        
        if name == "ï»¿player": #needed to skip the initial row of params
            continue

        #Finds stat leaders for events
        if kdCurr > kdLeader:   #KD Leader
            kdLeader3 = kdLeader2
            kdLeaderName3 = kdLeaderName2
            kdLeader2 = kdLeader
            kdLeaderName2 = kdLeaderName
            kdLeader = kdCurr
            kdLeaderName = name
        elif kdCurr > kdLeader2:
            kdLeader3 = kdLeader2
            kdLeaderName3 = kdLeaderName2
            kdLeader2 = kdCurr
            kdLeaderName2 = name
        elif kdCurr > kdLeader3:
            kdLeader3 = kdCurr
            kdLeaderName3 = name

        if kprCurr > kprLeader: #KPR Leader
            kprLeader3 = kprLeader2
            kprLeaderName3 = kprLeaderName2
            kprLeader2 = kprLeader
            kprLeaderName2 = kprLeaderName
            kprLeader = kprCurr
            kprLeaderName = name
        elif kprCurr > kprLeader2:
            kprLeader3 = kprLeader2
            kprLeaderName3 = kprLeaderName2
            kprLeader2 = kprCurr
            kprLeaderName2 = name
        elif kprCurr > kprLeader3:
            kprLeader3 = kprCurr
            kprLeaderName3 = name

        if adrCurr > adrLeader: #ADR Leader - bugs out with adr over 99.99???
            adrLeader3 = adrLeader2
            adrLeaderName3 = adrLeaderName2
            adrLeader2 = adrLeader
            adrLeaderName2 = adrLeaderName
            adrLeader = adrCurr
            adrLeaderName = name
        elif adrCurr > adrLeader2:
            adrLeader3 = adrLeader2
            adrLeaderName3 = adrLeaderName2
            adrLeader2 = adrCurr
            adrLeaderName2 = name
        elif adrCurr > adrLeader3:
            adrLeader3 = adrCurr
            adrLeaderName3 = name

        if hspCurr > hspLeader: #HSP Leader
            hspLeader3 = hspLeader2
            hspLeaderName3 = hspLeaderName2
            hspLeader2 = hspLeader
            hspLeaderName2 = hspLeaderName
            hspLeader = hspCurr
            hspLeaderName = name
        elif hspCurr > hspLeader2:
            hspLeader3 = hspLeader2
            hspLeaderName3 = hspLeaderName2
            hspLeader2 = hspCurr
            hspLeaderName2 = name
        elif hspCurr > hspLeader3:
            hspLeader3 = hspCurr
            hspLeaderName3 = name

        if dprCurr < dprLeader: #DPR Leader... Lower is better
            dprLeader3 = dprLeader2
            dprLeaderName3 = dprLeaderName2
            dprLeader2 = dprLeader
            dprLeaderName2 = dprLeaderName
            dprLeader = dprCurr
            dprLeaderName = name
        elif dprCurr < dprLeader2:
            dprLeader3 = dprLeader2
            dprLeaderName3 = dprLeaderName2
            dprLeader2 = dprCurr
            dprLeaderName2 = name
        elif dprCurr < dprLeader3:
            dprLeader3 = dprCurr
            dprLeaderName3 = name

        if udrCurr > udrLeader:
            udrLeader3 = udrLeader2
            udrLeaderName3 = udrLeaderName2
            udrLeader2 = udrLeader
            udrLeaderName2 = udrLeaderName
            udrLeader = udrCurr
            udrLeaderName = name
        elif udrCurr > udrLeader2:
            udrLeader3 = udrLeader2
            udrLeaderName3 = udrLeaderName2
            udrLeader2 = udrCurr
            udrLeaderName2 = name
        elif udrCurr > udrLeader3:
            udrLeader3 = udrCurr
            udrLeaderName3 = name



        if efrCurr > efrLeader:
            efrLeader3 = efrLeader2
            efrLeaderName3 = efrLeaderName2
            efrLeader2 = efrLeader
            efrLeaderName2 = efrLeaderName
            efrLeader = efrCurr
            efrLeaderName = name
        elif efrCurr > efrLeader2:
            efrLeader3 = efrLeader2
            efrLeaderName3 = efrLeaderName2
            efrLeader2 = efrCurr
            efrLeaderName2 = name
        elif efrCurr > efrLeader3:
            efrLeader3 = efrCurr
            efrLeaderName3 = name




        #MVP, EVPs, Winners
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

    print()
    print("--------------------------------")
    print()
    print("Stats leaders for event:")
    print("KD:  " + kdLeaderName + ", " + kdLeader + "  | " + kdLeaderName2 + ", " + kdLeader2 + " | " + kdLeaderName3 + ", " + kdLeader3)
    print("KPR: " + kprLeaderName + ", " + kprLeader + " | " + kprLeaderName2 + ", " + kprLeader2 + " | " + kprLeaderName3 + ", " + kprLeader3)
    print("DPR: " + dprLeaderName + ", " + dprLeader + " | " + dprLeaderName2 + ", " + dprLeader2 + " | " + dprLeaderName3 + ", " + dprLeader3)
    print("ADR: " + adrLeaderName + ", " + adrLeader + " | " + adrLeaderName2 + ", " + adrLeader2 + " | " + adrLeaderName3 + ", " + adrLeader3)
    print("HS%: " + hspLeaderName + ", " + hspLeader + "% | " + hspLeaderName2 + ", " + hspLeader2 + "% | " + hspLeaderName3 + ", " + hspLeader3 + "%")
    print("UDR: " + udrLeaderName + ", " + udrLeader + " | " + udrLeaderName2 + ", " + udrLeader2 + " | " + udrLeaderName3 + ", " + udrLeader3)
    print("EFR: " + efrLeaderName + ", " + efrLeader + " | " + efrLeaderName2 + ", " + efrLeader2 + " | " + efrLeaderName3 + ", " + efrLeader3)

eventStats()
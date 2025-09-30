import csv, os

currDir = os.path.dirname(os.path.abspath(__file__))
currDirEntries = os.listdir(currDir)
currDirFiles = [f for f in currDirEntries if os.path.isfile(os.path.join(currDir, f))]
nest = []

def eventSelect():
    print("Here is a list of available tournies: ")
    for fileName in currDirFiles:
        if fileName.endswith(".csv"):
            print(fileName, end = "\t")
    print("AllCombined\tAllSeparate")
    while True: #Used to select tournament from specified options in working dir
        try:
            tourneyName = input("Enter the name of the file you want to access. All options show lifetime stats, either combined or separate. Exit terminates the program.\n")
            tourneyName = tourneyName.lower()
            if tourneyName.endswith(".csv"):
                for fileName in currDirFiles:
                    if tourneyName == fileName:
                        print("Gathering data for specified tourney...")
                break
            elif tourneyName == "allcombined":
                print("Gathering combined stats from tournaments...")
                break
            elif tourneyName == "allseparate":
                print("Gathering stats from tournaments...")
                break
            elif tourneyName == "exit":
                exit()
            else:
                print("Input invalid, please try again.")      
        finally:
            print("")
    return tourneyName

tourney = eventSelect()

def getStats():
    if tourney == "allcombined":
        dups = []
        for fileName in currDirFiles:
            if fileName.endswith(".csv"):
                stats = open(fileName, 'r')
                for name in stats:
                    rows = name.split(",")
                    if rows[0] in dups:
                        entryCount = 0
                        for entries in nest:
                            if rows[0] == entries[0] and rows[0] != "ï»¿player":
                                entries[1] = str(int(rows[1])+int(entries[1])) #k
                                entries[2] = str(int(rows[2])+int(entries[2])) #hs
                                entries[3] = str(int(rows[3])+int(entries[3])) #d
                                entries[4] = str(int(rows[4])+int(entries[4])) #ud
                                entries[5] = str(int(rows[5])+int(entries[5])) #ef
                                entries[6] = str(int(rows[6])+int(entries[6])) #dam
                                entries[7] = str(int(rows[7])+int(entries[7])) #r
                                entries[8] = str(round(int(entries[1])/int(entries[7]), 2)) #kpr
                                entries[9] = str(round(int(entries[3])/int(entries[7]), 2)) #dpr
                                entries[10] = str(round(int(entries[4])/int(entries[7]), 2)) #udr
                                entries[11] = str(round(int(entries[5])/int(entries[7]), 2)) #efr
                                entries[12] = str(round(int(entries[1])/int(entries[3]), 2)) #kd
                                entries[13] = str(round(int(entries[2])/int(entries[1]), 4)*100) #hsp
                                entries[14] = str(round(int(entries[6])/int(entries[7]), 2)) #adr
                                if rows[15] == "1st":
                                    entries[15] = "1st"
                                if rows[16] != "none":
                                    if rows[16] == "MVP\n" and entries[16] != "MVP\n":
                                        entries[16] = "MVP\n"
                                    if rows[16] == "EVP\n" and entries[16] == "none\n":
                                        entries[16] = "EVP\n"
                            entryCount +=1
                    else:
                        nest.append(rows)
                        dups.append(rows[0])
                stats.close()
    elif tourney == "allseparate":
        for fileName in currDirFiles:
            if fileName.endswith(".csv"):
                stats = open(fileName, 'r')
                for name in stats:
                    rows = name.split(",")
                    nest.append(rows)
                stats.close()
    else:
        stats = open(tourney, 'r')
        for name in stats:
            rows = name.split(",")
            nest.append(rows)
        stats.close()

    rowCounter = 0
    for row in nest:    #Delete Generic Row
        if row[0] == "ï»¿player" or row[0] == "player":
            nest.pop(rowCounter)
        rowCounter +=1

def HSpercentage(player):
    return nest[player][13]

def ADR(player):
    return nest[player][14]

def KPR(player):
    return nest[player][8] 
  
def DPR(player):
    return nest[player][9]

def EFR(player): 
    return nest[player][11]

def UDR(player):
    return nest[player][10]

def KD(player):
    return nest[player][12]

def Rounds(player):
    return nest[player][7]
              
def playerStats(player, index):
    print(player + "'s stats over " + Rounds(index) + " rounds:")
   
    print("KD: " + KD(index))
    print("ADR: " + ADR(index))
    print("HS%: " + HSpercentage(index))

    print("KPR: " + KPR(index))
    print("DPR: " + DPR(index))

    print("UDR: " + UDR(index))
    print("EFR: " + EFR(index))

def eventStats():
    winners = []
    EVPs = []
    MVPs = []
    MVP = ""
    MVPIndex, indexCount = 0, 0
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

    print("Summary of stats for " + tourney + ":")
    print()
    for row in nest:
        name = row[0]
        kdCurr, adrCurr, hspCurr = KD(indexCount), ADR(indexCount), HSpercentage(indexCount)
        kprCurr, dprCurr = KPR(indexCount), DPR(indexCount)
        udrCurr, efrCurr = UDR(indexCount), EFR(indexCount)

        if float(kdCurr) > float(kdLeader):
            kdLeader3 = kdLeader2
            kdLeaderName3 = kdLeaderName2
            kdLeader2 = kdLeader
            kdLeaderName2 = kdLeaderName
            kdLeader = kdCurr
            kdLeaderName = name
        elif float(kdCurr) > float(kdLeader2):
            kdLeader3 = kdLeader2
            kdLeaderName3 = kdLeaderName2
            kdLeader2 = kdCurr
            kdLeaderName2 = name
        elif float(kdCurr) > float(kdLeader3):
            kdLeader3 = kdCurr
            kdLeaderName3 = name

        if kprCurr > kprLeader:
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

        if float(adrCurr) > float(adrLeader):
            adrLeader3 = adrLeader2
            adrLeaderName3 = adrLeaderName2
            adrLeader2 = adrLeader
            adrLeaderName2 = adrLeaderName
            adrLeader = adrCurr
            adrLeaderName = name
        elif float(adrCurr) > float(adrLeader2):
            adrLeader3 = adrLeader2
            adrLeaderName3 = adrLeaderName2
            adrLeader2 = adrCurr
            adrLeaderName2 = name
        elif float(adrCurr) > float(adrLeader3):
            adrLeader3 = adrCurr
            adrLeaderName3 = name

        if float(hspCurr) > float(hspLeader):
            hspLeader3 = hspLeader2
            hspLeaderName3 = hspLeaderName2
            hspLeader2 = hspLeader
            hspLeaderName2 = hspLeaderName
            hspLeader = hspCurr
            hspLeaderName = name
        elif float(hspCurr) > float(hspLeader2):
            hspLeader3 = hspLeader2
            hspLeaderName3 = hspLeaderName2
            hspLeader2 = hspCurr
            hspLeaderName2 = name
        elif float(hspCurr) > float(hspLeader3):
            hspLeader3 = hspCurr
            hspLeaderName3 = name

        if dprCurr < dprLeader:
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

        if float(udrCurr) > float(udrLeader):
            udrLeader3 = udrLeader2
            udrLeaderName3 = udrLeaderName2
            udrLeader2 = udrLeader
            udrLeaderName2 = udrLeaderName
            udrLeader = udrCurr
            udrLeaderName = name
        elif float(udrCurr) > float(udrLeader2):
            udrLeader3 = udrLeader2
            udrLeaderName3 = udrLeaderName2
            udrLeader2 = udrCurr
            udrLeaderName2 = name
        elif float(udrCurr) > float(udrLeader3):
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

        if row[16] == "MVP\n": 
            MVP = name
            MVPIndex = indexCount
            MVPs.append(MVP)
        indexCount+=1
        if row[16] == "EVP\n":
            EVPs.append(name)
        if row[15] == "1st":
            winners.append(name)

    if tourney == "allcombined" or tourney == "allseparate":
        print("Winners: ", end = "")
        personCount = 0
        for person in winners:
            print(winners[personCount], end = " ")
            if personCount%2 == 1 and personCount != (len(winners)-1):
                print("|", end = " ")
            if personCount%2 == 0:
                print("&", end = " ")
            personCount +=1
        print()
        print("MVPs:", end = " ")
        for index in MVPs:
            if index == MVPs[-1]:
                print("& " + index)
            elif len(MVPs) == 2:
                print(index, end = " ")
            else:
                print(index, end = ", ")
    else:
        print("Winners: " + winners[0] + " & " + winners[1])
        print()
        print("MVP: " + MVP)
        playerStats(MVP, MVPIndex)
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
    print("Stats leaders for event " + tourney + ":")
    print("KD:  " + kdLeaderName + ": " + kdLeader + "  | " + kdLeaderName2 + ": " + kdLeader2 + " | " + kdLeaderName3 + ": " + kdLeader3)
    print("KPR: " + kprLeaderName + ": " + kprLeader + " | " + kprLeaderName2 + ": " + kprLeader2 + " | " + kprLeaderName3 + ": " + kprLeader3)
    print("DPR: " + dprLeaderName + ": " + dprLeader + " | " + dprLeaderName2 + ": " + dprLeader2 + " | " + dprLeaderName3 + ": " + dprLeader3)
    print("ADR: " + adrLeaderName + ": " + adrLeader + " | " + adrLeaderName2 + ": " + adrLeader2 + " | " + adrLeaderName3 + ": " + adrLeader3)
    print("HS%: " + hspLeaderName + ": " + hspLeader + "% | " + hspLeaderName2 + ": " + hspLeader2 + "% | " + hspLeaderName3 + ": " + hspLeader3 + "%")
    print("UDR: " + udrLeaderName + ": " + udrLeader + " | " + udrLeaderName2 + ": " + udrLeader2 + " | " + udrLeaderName3 + ": " + udrLeader3)
    print("EFR: " + efrLeaderName + ": " + efrLeader + " | " + efrLeaderName2 + ": " + efrLeader2 + " | " + efrLeaderName3 + ": " + efrLeader3)

getStats()
eventStats()
print()
while True:
    playerName = input("Type a player's name to get their stats, 'back' to go to tournament selection, or 'exit' to terminate.")
    if playerName == "back":
        nest.clear()
        tourney = eventSelect()
        getStats()
        eventStats()
        print()
    elif playerName == "exit":
        exit()
    else:
        timesPrinted = 0
        index = -1
        for row in nest:
            index+=1 
            if row[0] == playerName:
                playerStats(playerName, index)
                if tourney == "allseparate":
                    print()
                    timesPrinted +=1
                else:
                    print()
                    break
            elif row[0] != playerName and row == nest[-1] and timesPrinted == 0:
                print("Name not recognized, here are available options: ", end = "")
                for row in nest:
                    print(row[0], end = " ")
                print()
            else:
                continue
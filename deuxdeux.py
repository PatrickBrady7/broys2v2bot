import os

currDir = os.path.dirname(os.path.abspath(__file__))
currDirFiles = [f for f in os.listdir(currDir) if os.path.isfile(os.path.join(currDir, f))]
nest = []

def eventSelect():
    print("Here is a list of available tournies: ")
    for fileName in currDirFiles:
        if fileName.endswith(".csv"):
            print(fileName, end = "\t")
    print("Combined\tSeparate")
    while True: #Used to select tournament from specified options in working dir
        try:
            tourneyName = input("Enter the name of the file you want to access. Other options show lifetime stats, either combined or separate. Exit terminates the program.\n")
            tourneyName = tourneyName.lower()
            if tourneyName.endswith(".csv"):
                for fileName in currDirFiles:
                    if tourneyName == fileName:
                        print("Gathering data for specified tourney...")
                break
            elif tourneyName == "combined":
                print("Gathering combined stats from tournaments...")
                break
            elif tourneyName == "separate":
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
    if tourney == "combined":
        dups = []
        for fileName in currDirFiles:
            if fileName.endswith(".csv"):
                stats = open(fileName, 'r')
                for name in stats:
                    rows = name.split(",")
                    if rows[0] in dups:
                        entryCount = 0
                        for entries in nest:
                            if rows[0] == entries[0] and rows[0] != "player":
                                entries[1] = str(int(rows[1])+int(entries[1])) #k
                                entries[2] = str(int(rows[2])+int(entries[2])) #hs
                                entries[3] = str(int(rows[3])+int(entries[3])) #mk
                                entries[4] = str(int(rows[4])+int(entries[4])) #1v2s
                                entries[5] = str(int(rows[5])+int(entries[5])) #d
                                entries[6] = str(int(rows[6])+int(entries[6])) #ud
                                entries[7] = str(int(rows[7])+int(entries[7])) #ef
                                entries[8] = str(int(rows[8])+int(entries[8])) #dam
                                entries[9] = str(int(rows[9])+int(entries[9])) #r
                                entries[10] = str(round(int(entries[1])/int(entries[9]), 2)) #kpr
                                entries[11] = str(round(int(entries[4])/int(entries[9]), 2)) #1v2pr
                                entries[12] = str(round(int(entries[3])/int(entries[9]), 2)) #mkpr
                                entries[13] = str(round(int(entries[5])/int(entries[9]), 2)) #dpr
                                entries[14] = str(round(int(entries[6])/int(entries[9]), 2)) #udr
                                entries[15] = str(round(int(entries[7])/int(entries[9]), 2)) #efr
                                entries[16] = str(round(int(entries[1])/int(entries[5]), 2)) #kd
                                entries[17] = str(round(int(entries[2])/int(entries[1]), 4)*100) #hsp
                                entries[18] = str(round(int(entries[8])/int(entries[9]), 2)) #adr
                                if rows[19] == "1st":
                                    entries[19] = "1st"
                                if rows[20] != "none":
                                    if rows[20] == "MVP" and entries[20] != "MVP":
                                        entries[20] = "MVP"
                                    if rows[20] == "EVP" and entries[20] == "none":
                                        entries[20] = "EVP"
                                #entries[21] = rows[21]+entries[21] #PadRating
                                entries[21] = str((1 + ((float(entries[10])/2) + (float(entries[12])/4) + (float(entries[11])/5) - (float(entries[13])) + (float(entries[18])/215) + (float(entries[15])/20)))) #PadRating
                            entryCount +=1
                    else:
                        nest.append(rows)
                        dups.append(rows[0])
                stats.close()
    elif tourney == "separate":
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
    return nest[player][17]

def ADR(player):
    return nest[player][18]

def KPR(player):
    return nest[player][10] 
  
def DPR(player):
    return nest[player][13]

def EFR(player): 
    return nest[player][15]

def UDR(player):
    return nest[player][14]

def KD(player):
    return nest[player][16]

def Rounds(player):
    return nest[player][9]

def PadRating(player):
    return nest[player][21]

def MKPR(player):
    return nest[player][12]

def OvTPR(player):
    return nest[player][11]

def playerStats(player, index):
    print(player + "'s stats over " + Rounds(index) + " rounds:")
    print("PadRating: " + PadRating(index)[:4])
    print()
    print("KD: " + KD(index))
    print("HS%: " + HSpercentage(index))    
    print("ADR: " + ADR(index))
    print("KPR: " + KPR(index))
    print("DPR: " + DPR(index))
    print()
    print("MKPR: " + MKPR(index))
    print("1v2PR: " + OvTPR(index))
    print("UDR: " + UDR(index))
    print("EFR: " + EFR(index) + "\n")

def eventStats():
    winners = []
    EVPs = []
    MVPs = []
    MVP = ""
    MVPIndex, rowIndex = 0, 0
    PadRatingLeader, PadRatingLeader2, PadRatingLeader3= "0", "0", "0"
    kdLeader, kdLeader2, kdLeader3= "0", "0", "0"
    kprLeader, kprLeader2, kprLeader3 = "0", "0", "0"
    adrLeader, adrLeader2, adrLeader3 = "0", "0", "0"
    hspLeader, hspLeader2, hspLeader3 = "0", "0", "0"
    dprLeader, dprLeader2, dprLeader3 = "1", "1", "1"
    udrLeader, udrLeader2, udrLeader3 = "0", "0", "0"
    efrLeader, efrLeader2, efrLeader3 = "0", "0", "0"
    mkprLeader, mkprLeader2, mkprLeader3 = "0", "0", "0"
    ovtprLeader, ovtprLeader2, ovtprLeader3 = "0", "0", "0"
    PadRatingLeaderName, PadRatingLeaderName2, PadRatingLeaderName3 = "", "", ""
    kdLeaderName, kdLeaderName2, kdLeaderName3 = "", "", ""
    kprLeaderName, kprLeaderName2, kprLeaderName3 = "", "", ""
    adrLeaderName, adrLeaderName2, adrLeaderName3 = "", "", ""
    hspLeaderName, hspLeaderName2, hspLeaderName3 = "", "", ""
    dprLeaderName, dprLeaderName2, dprLeaderName3 = "", "", ""
    udrLeaderName, udrLeaderName2, udrLeaderName3 = "", "", ""
    efrLeaderName, efrLeaderName2, efrLeaderName3 = "", "", ""
    mkprLeaderName, mkprLeaderName2, mkprLeaderName3 = "", "", ""
    ovtprLeaderName, ovtprLeaderName2, ovtprLeaderName3 = "", "", ""

    print("Summary of stats for " + tourney + ":\n")
    for row in nest:
        name = row[0]
        PadRatingCurr, kdCurr, adrCurr, hspCurr = PadRating(rowIndex), KD(rowIndex), ADR(rowIndex), HSpercentage(rowIndex)
        kprCurr, dprCurr = KPR(rowIndex), DPR(rowIndex)
        udrCurr, efrCurr = UDR(rowIndex), EFR(rowIndex)
        mkprCurr, ovtprCurr = MKPR(rowIndex), OvTPR(rowIndex)

        if float(PadRatingCurr) > float(PadRatingLeader):
            PadRatingLeader3 = PadRatingLeader2
            PadRatingLeaderName3 = PadRatingLeaderName2
            PadRatingLeader2 = PadRatingLeader
            PadRatingLeaderName2 = PadRatingLeaderName
            PadRatingLeader = PadRatingCurr
            PadRatingLeaderName = name
        elif float(PadRatingCurr) > float(PadRatingLeader2):
            PadRatingLeader3 = PadRatingLeader2
            PadRatingLeaderName3 = PadRatingLeaderName2
            PadRatingLeader2 = PadRatingCurr
            PadRatingLeaderName2 = name
        elif float(PadRatingCurr) > float(PadRatingLeader3):
            PadRatingLeader3 = PadRatingCurr
            PadRatingLeaderName3 = name

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

        if mkprCurr > mkprLeader:
            mkprLeader3 = mkprLeader2
            mkprLeaderName3 = mkprLeaderName2
            mkprLeader2 = mkprLeader
            mkprLeaderName2 = mkprLeaderName
            mkprLeader = mkprCurr
            mkprLeaderName = name
        elif mkprCurr > mkprLeader2:
            mkprLeader3 = mkprLeader2
            mkprLeaderName3 = mkprLeaderName2
            mkprLeader2 = mkprCurr
            mkprLeaderName2 = name
        elif mkprCurr > mkprLeader3:
            mkprLeader3 = mkprCurr
            mkprLeaderName3 = name

        if ovtprCurr > ovtprLeader:
            ovtprLeader3 = ovtprLeader2
            ovtprLeaderName3 = ovtprLeaderName2
            ovtprLeader2 = ovtprLeader
            ovtprLeaderName2 = ovtprLeaderName
            ovtprLeader = ovtprCurr
            ovtprLeaderName = name
        elif ovtprCurr > ovtprLeader2:
            ovtprLeader3 = ovtprLeader2
            ovtprLeaderName3 = ovtprLeaderName2
            ovtprLeader2 = ovtprCurr
            ovtprLeaderName2 = name
        elif ovtprCurr > ovtprLeader3:
            ovtprLeader3 = ovtprCurr
            ovtprLeaderName3 = name

        if row[20] == "MVP": 
            MVP = name
            MVPIndex = rowIndex
            MVPs.append(MVP)
        rowIndex+=1
        if row[20] == "EVP":
            EVPs.append(name)
        if row[19] == "1st":
            winners.append(name)

    if tourney == "combined" or tourney == "separate":
        print("Winners: ", end = "")
        personCount = 0
        for _ in winners:
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
        print("Winners: " + winners[0] + " & " + winners[1] + "\n")
        print("MVP: " + MVP)
        playerStats(MVP, MVPIndex)
    
    print("EVPs:" , end =" ")
    for index in EVPs:
        if index == EVPs[-1]:
            print("& " + index)
        else:
            print(index, end = ", ")

    PadRatingLeader = round(float(PadRatingLeader), 2)
    PadRatingLeader2 = round(float(PadRatingLeader2), 2)
    PadRatingLeader3 = round(float(PadRatingLeader3), 2)

    PadRatingLeader = str(PadRatingLeader)
    PadRatingLeader2 = str(PadRatingLeader2)
    PadRatingLeader3 = str(PadRatingLeader3)

    print("\n--------------------------------\n")
    print("Stats leaders for event " + tourney + ":")
    print("PadRating:  " + PadRatingLeaderName + ": " + PadRatingLeader + "  | " + PadRatingLeaderName2 + ": " + PadRatingLeader2 + " | " + PadRatingLeaderName3 + ": " + PadRatingLeader3)
    print("KD:  " + kdLeaderName + ": " + kdLeader + "  | " + kdLeaderName2 + ": " + kdLeader2 + " | " + kdLeaderName3 + ": " + kdLeader3)
    print("KPR: " + kprLeaderName + ": " + kprLeader + " | " + kprLeaderName2 + ": " + kprLeader2 + " | " + kprLeaderName3 + ": " + kprLeader3)
    print("DPR: " + dprLeaderName + ": " + dprLeader + " | " + dprLeaderName2 + ": " + dprLeader2 + " | " + dprLeaderName3 + ": " + dprLeader3)
    print("ADR: " + adrLeaderName + ": " + adrLeader + " | " + adrLeaderName2 + ": " + adrLeader2 + " | " + adrLeaderName3 + ": " + adrLeader3)
    print("HS%: " + hspLeaderName + ": " + hspLeader + "% | " + hspLeaderName2 + ": " + hspLeader2 + "% | " + hspLeaderName3 + ": " + hspLeader3 + "%")
    print("MKPR: " + mkprLeaderName + ": " + mkprLeader + " | " + mkprLeaderName2 + ": " + mkprLeader2 + " | " + mkprLeaderName3 + ": " + mkprLeader3)
    print("1v2PR: " + ovtprLeaderName + ": " + ovtprLeader + " | " + ovtprLeaderName2 + ": " + ovtprLeader2 + " | " + ovtprLeaderName3 + ": " + ovtprLeader3)
    print("UDR: " + udrLeaderName + ": " + udrLeader + " | " + udrLeaderName2 + ": " + udrLeader2 + " | " + udrLeaderName3 + ": " + udrLeader3)
    print("EFR: " + efrLeaderName + ": " + efrLeader + " | " + efrLeaderName2 + ": " + efrLeader2 + " | " + efrLeaderName3 + ": " + efrLeader3 + "\n")

getStats()
eventStats()
while True:
    playerName = input("Type a player's name to get their stats, 'back' to go to tournament selection, or 'exit' to terminate.")
    if playerName == "back":
        nest.clear()
        tourney = eventSelect()
        getStats()
        eventStats()
    elif playerName == "exit":
        exit()
    else:
        timesPrinted = 0
        index = -1
        for row in nest:
            index+=1 
            if row[0] == playerName:
                playerStats(playerName, index)
                if tourney == "separate":
                    timesPrinted +=1
                else:
                    break
            elif row[0] != playerName and row == nest[-1] and timesPrinted == 0:
                print("Name not recognized, here are available options: ", end = "")
                for row in nest:
                    print(row[0], end = " ")
                print()
            else:
                continue
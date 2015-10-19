# -*- coding: utf-8 -*

def montant_en_lettres(montant):
    stmount = str(montant)
    maliste = stmount.split(".")
    stmount = maliste[0]
    intdecim = ""
    if len(maliste) == 2 and maliste[1] not in ("0","00"):
        decim = maliste[1]
        intdecim = int(decim)
        
    l = len(stmount)
    if montant == "1":
        plur = ""
    else:
        plur = "s"
    devise = "dinar" + plur
    
    chaine = ""
    
    liste1 = {"0":"",
                    "1":"un",
                    "2":"deux",
                    "3":"trois",
                    "4":"quatre",
                    "5":"cinq",
                    "6":"six",
                    "7":"sept",
                    "8":"huit",
                    "9":"neuf",
                    "10":"dix",
                    "11":"onze",
                    "12":"douze",
                    "13":"treize",
                    "14":"quatorze",
                    "15":"quinze",
                    "16":"seize",
                    "17":"dix-sept",
                    "18":"dix-huit",
                    "19":"dix-neuf"
                    }
        
    liste2 = {"1":"dix",
                 "2":"vingt",
                 "3":"trente",
                 "4":"quarante",
                 "5":"cinquante",
                 "6":"soixante",
                 "7":"soixante-dix",
                 "8":"quatre-vingt",
                 "9":"quatre-vingt-dix"
                 }
    def trans100(mount):
        
        def trans1(num):
            numc = ""
            if num < 20:
                a = str(num)
                numc = liste1[a]
                return numc
            
            elif num >=20 and num < 71 or num >= 80 and num < 91:
                b = str(num)
                a = b[0]
                c = b[1]
                if c == "1":
                    numc = liste2[a] + " et " + liste1[c]
                elif c == "0":
                    numc = liste2[a]
                else:    
                    numc = liste2[a] + " " + liste1[c]
                    
                return numc
            
            elif num >= 71 and num < 80:
                b71 = str(num)
                d71 = b71[0]
                a71 = str(int(d71) - 1)
                c71 = "1" + b71[1]
                if c71 == "11":
                    numc = liste2[a71] + " et " + liste1[c71]
                else:
                    numc = liste2[a71] + " " + liste1[c71]
                
                return numc
            
            elif num >= 91 and num < 100:
                b91 = str(num)
                d91 = b91[0]
                a91 = str(int(d91) - 1)
                c91 = "1" + b91[1]
                if c91 == "11":
                    numc = liste2[a91] + " et " + liste1[c91]
                else:
                    numc = liste2[a91] + " " + liste1[c91]
                
                return numc
    
        mountc = ""
        if mount == 100:
            return "cent"
        elif mount < 100:
            mountc = trans1(mount)
            return mountc
        else:     
            a100 = str(mount)
            b100 = a100[0]
            c100 = a100[-2:]
            d100 = liste1[b100]
            e100 = int(c100)
            f100 = trans1(e100)
            
            if d100 == "un":
                mountc = "cent " + f100
            else:
                mountc = d100 + " cent " + f100
            
            return mountc            
# Analyser les groupes de trois chiffres:
    if intdecim:
        intdecim = " et " + trans100(intdecim) + " centime(s)"
    
    if l >= 1 and l < 4:
        part = stmount
        intpart = int(part)
        chaine = trans100(intpart) + " "
        
    elif l >= 4 and l < 7:
        part1 = stmount[:-3]
        part0 = stmount[-3:]
        if part1 == "1":
            plur1 = ""
        else:
            plur1 = "s"
        unit1 = "mille" + plur1 + " "

        intpart0 = int(part0)
        intpart1 = int(part1)
        if part1 == "1":
            trpart1 = unit1
        else:
            trpart1 = trans100(intpart1) + " " + unit1
        trpart0 = trans100(intpart0)
        
        chaine = trpart1 + trpart0 + " "
        
    elif l >= 7 and l < 10:
        unit2 = ""
        unit1 = ""
        part2 = stmount[:-6]
        part1 = stmount[-6:-3]
        part0 = stmount[-3:]
        if part1 == "000":
            det2 = " de"
        else:
            det2 = ""
        if part1 == "001":
            plur1 = ""
        else:
            plur1 = "s"
        if part2 == "1":
            plur2 = ""
        else:
            plur2 = "s"

        if part2 != "000":
            unit2 = " million" + plur2 + det2 + " "
        
        if part1 != "000":
            unit1 = " mille" + plur1 + " "
        if part0 != "000":
            unit0 = " "
        intpart2 = int(part2)
        trpart2 = trans100(intpart2) + unit2
        intpart1 = int(part1)
        trpart1 = trans100(intpart1) + unit1
        intpart0 = int(part0)
        trpart0 = trans100(intpart0) + unit0
        chaine = trpart2 + trpart1 + trpart0
        
    elif l >= 10:
        part0 = stmount[-3:]
        part1 = stmount[-6:-3]
        part2 = stmount[-9:-6]
        part3 = stmount[:-9]
        
        if part2 == "000" and part1 == "000":
            det3 = " de"
        else:
            det3 = ""

        if part1 == "000":
            det2 = " de"
        else:
            det2 = ""
            
        if part3 == "1":
            plur3 = ""
        else:
            plur3 = "s"
        if part2 == "1":
            plur2 = ""
        else:
            plur2 = "s"
        if part1 == "1":
            plur1 = ""
        else:
            plur1 = "s"
        unit3 = " milliard" + plur3 + det3 + " "
        unit2 = ""
        unit1 = ""

        if part2 != "000":
            unit2 = " million" + plur2 + det2 + " "

        if part1 != "000":
            unit1 = " mille" + plur1 + " "
            
        if part0 != "000":
            unit0 = " "

        intpart3 = int(part3)
        trpart3 = trans100(intpart3) + unit3
        intpart2 = int(part2)
        trpart2 = trans100(intpart2) + unit2
        intpart1 = int(part1)
        trpart1 = trans100(intpart1) + unit1
        intpart0 = int(part0)
        trpart0 = trans100(intpart0) + unit0
    
        chaine = trpart3 + trpart2 + trpart1 + trpart0
    strdecim = str(intdecim)
    ml = (chaine, strdecim)
    return ml
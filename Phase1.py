import sys


def GetFileName():
    if (len(sys.argv) != 2):
        print('Invalid command line.')
        sys.exit()
    fname = sys.argv[1]
    return fname



def substraction(line, str1, str2):
    index1 = -1
    index1 = line.find(str1)
    index2 = line.find(str2)
    if (index1!= -1):
        if (index2 > index1 + len(str1)):
            return line[index1 + len(str1): index2]
        else:
            return -1
    return -1   



def simplified(outputfile, wlist, aid):
    if (wlist == -1):
        return 0
    #print(type(wlist))
    str1 = '&#'
    str2 = ';'
    str5 = '&apos;'
    str4 = '&quot;'
    str3 = '&amp;'
    
    while(1):
        index1 = wlist.find(str1)
        if (index1 == -1):
            break
        templist = wlist[index1:]
        index2 = templist.find(str2)
        if (index2 != -1):
            word = wlist[index1 + len(str1): index2+len(wlist)-len(templist)]
            
            if (word.isdigit()):
                wlist = wlist[:index1] +  wlist[index2+len(wlist)-len(templist)+1:]
            else:
                index1 = wlist.find(str1)
                wlist = wlist.replace(str1, '  ')
                index2 = wlist.find(str2)
                wlist = wlist.replace(str1, ' ')
            
        
    while(1):
        index1 = wlist.find(str3)
        if (index1 == -1):
            break
        wlist = wlist.replace(str3, ' ')
        
        
    while(1):
        index1 = wlist.find(str4)
        if (index1 == -1):
            break
        wlist = wlist.replace(str4, ' ')


    while(1):
        index1 = wlist.find(str5)
        if (index1 == -1):
            break
        wlist = wlist.replace(str5, ' ')    


    for w in wlist:
        if (w.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789-_'):
            wlist = wlist.replace(w, ' ')
            
            
    wlist = wlist.split()
    nlist = []
    for term in wlist:
        if (len(term) > 2):
            nlist.append(term.lower())
            outputfile.write(term.lower() + ':' + aid + '\n' )
    return 0



def pdates(outputfile, date, aid, category, location):
    if(date == -1):
        return 0
    outputfile.write(date + ':' + aid + ',' + category + ',' + location + '\n' )
    return 0



def prices(outputfile, price, aid, category, location):
    if (price == -1):
        return 0
    else:
        outputfile.write(price.rjust(12, ' ') + ':' + aid + ',' + category + ',' + location + '\n' )
        return 0



def ads(outputfile, aid, line):
    outputfile.write(aid + ':' + line)
    return 0
    

        
def main():
    fname = GetFileName()    
    infile = open(fname, 'r')
    outfile1 = open('terms.txt', 'w')
    outfile2 = open('pdates.txt', 'w')
    outfile3 = open('prices.txt', 'w')
    outfile4 = open('ads.txt', 'w')
    for line in infile:
        aid = substraction(line, '<aid>', '</aid>')
        if (aid != -1):
            title = substraction(line, '<ti>', '</ti>')
            description = substraction(line, '<desc>', '</desc>')
            date = substraction(line, '<date>', '</date>')
            category = substraction(line, '<cat>', '</cat>')
            location = substraction(line, '<loc>', '</loc>')
            price = substraction(line, '<price>', '</price>')
            simplified(outfile1, title, aid)
            simplified(outfile1, description, aid)
            pdates(outfile2, date, aid, category, location)
            prices(outfile3, price, aid, category, location)
            ads(outfile4, aid, line)
    infile.close()
    outfile1.close()
    outfile2.close()
    outfile3.close()
    outfile4.close()
            
    return 0
    
main()

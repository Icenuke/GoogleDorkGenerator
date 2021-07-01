#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import argv
from os import getcwd, listdir

def HelpUsage():
    """
        Show an help message and short description of program
    """
    print("""Usage: Dork [-h] word1 word2 "words group" ... 
                    -h      Show this message
                    
                    Developed by Icenuke.
                    For more dork see this page:
                    https://www.exploit-db.com/google-hacking-database/?action=search&ghdb_search_cat_id=0&ghdb_search_text=google+dork
                    """)


def ExportResult(namePage, baseURL, resultLst):
    """
        This function export the result in HTML page with Hyperlink
        :param namePage:    name of export page
        :param resultLst:   list of result (urls to search)
        :return:            file with urls
    """
    # verify if the document already exist in the current path
    if namePage not in listdir(getcwd()):
        # if not exist create the document with the start html code
        with open(namePage, "a+") as exportResult:
            # exportResult.write("""<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<dork>\n<title>%s</title>\n""" % (namePage[:-4]))
            exportResult.write("%s\n\n" % (namePage[:-4]))

            # for the google result do this
            if namePage.find('Google') != -1:
                # iter in the list in the list
                for result in resultLst:
                    # declaration h3 and li return in default value in start loop
                    h3 = ""
                    li = baseURL

                    # iter in the list recovered start in 0 finish in len list -1 with padding 2
                    for n in range(0, len(result)-1, 2):
                        # concatenation of h3 and li
                        h3 += "[%s%s]" % (result[n].replace("%3A", ":"), result[n+1].replace("+", " "))
                        li += "%s%s+" % (result[n], result[n+1])

                    # write line with the format is good
                    exportResult.write("%s\n%s\n\n" % (h3, li))

            # if is shodan
            elif namePage.find('ShodanResearch') != -1:
                print()

    else:
        print("The export file: %s already exist!!\nMove this in other place or delete this.\n" % (namePage))




def GoogleDork(wordList):
    """
        This function forge urls with google dork and wordList passed in parameter
        And create a file with this urls
        :param wordList:    List of keyWord used to research in google
        :return:            list of urls
    """
    # list of google dork
    dork = ["intitle%3A",
            "inurl%3A",
            "intext%3A",
            "insubject%3A",
            "ext%3A",
            "filetype%3A",
            "site%3A",
            "author%3A",
            "group%3A",
            "%2B",
            "*"]

    # speDork =["|", "(%s | %s)"]

    # base url research Google
    googleUrl = "https://www.google.fr/search?q="

    """ 
        1. Iter in all wordlist and add "" in values if necessary
        2. Iter in 9 first dork
        3. Iter in 10 first dork
        4. Iter in all wordlist in second time
        5. Iter in all dork
        6. Iter in all wordlist in third time
        7. Call function to create in HTML page the list of urls create
        
    """
    # suppr space in value
    for n in range(len(wordList)):
        wordList[n] = wordList[n].replace(" ", "+")

    # if len(wordList)
    path = getcwd()

    result = [ [dork[i], fstWord, dork[k], scdWord, gd3, trdWord] for fstWord in wordList for i in range(len(dork)-2) for k in range(len(dork)-1) for scdWord in wordList for gd3 in dork for trdWord in wordList ]
    ExportResult(path+"\\GoogleDorkResult.txt", googleUrl, result)

    """ 
        1. Iter in all wordlist 
        2. Iter in 8 first dork
        3. Iter in 9 first dork
        4. Iter in all wordlist in second time
        5. Iter in 10 dork
        6. Iter in all wordlist in third time
        7. Iter in all dork
        8. Iter in all wordlist in four time
        9. Call function to create in HTML page the list of urls create

    """
    result2 = [[dork[i], fstWord, dork[j], scdWord, dork[k], trdWord, gd4, frWord] for fstWord in wordList for i in range(len(dork) - 3) for j in range(len(dork) - 2) for scdWord in wordList for k in range(len(dork)-1) for trdWord in wordList for gd4 in dork for frWord in wordList ]
    ExportResult(path+"\\GoogleDorkResult++.txt", googleUrl, result2)



if __name__ == "__main__":
    print("""
                                 ____    ___   ____   _   __
                                /_   \  / _ \ |  _ \ | | / /
                                  ||\ \| / \ || |_| || |/ /
                                  || ||| | | ||    / |   |
                                __||/ /| \_/ || |\ \ | |\ \ 
                                \____/  \___/ |_| \_\|_| \_\ 
                                            Developed by Icenuke.
    """)

    # check if arguments is in parameters
    if len(argv) > 1:
        if "-h" in argv:
            HelpUsage()

        # research in google with dork
        else:
            # clean list for the functions
            argv.remove(argv[0])

            # call function to forge urls
            GoogleDork(argv)

    else:
        # if error then show help message
        HelpUsage()



#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################
 
## Par Paul Besson
## Description : Url Checker 
## Dependances :
## Utilisation : python urlChecker.py path/to/list.txt path/to/result.txt
 
#############################


#############################
####### Libraries
#############################

import sys
import urllib
import urllib.request
from urllib.error import HTTPError, URLError
import socket
from socket import timeout

##################
### Fonctions
##################



##################
# Fontion > Get arguments
def checkFile():
	nbArgument = len(sys.argv)
	if nbArgument != 3:
		print ("Usage : python urlChecker.py path/to/list.txt path/to/result.txt")
		exit()
	else:
		# Init des parametres
		global fileList, fileOut
		fileList     = sys.argv[1]
		fileOut      = sys.argv[2]


##################
# Fontion > Get list URLs
def getList():
	# Liste des urls
	global listUrl
	listUrl = [line.rstrip() for line in open(fileList)]


##################
# Fontion > Test list URLs
def testList():
        # Tests des urls
	for urlCheck in listUrl :
	
		
		urlCheck = urlCheck + "/urlCheck"
		print(urlCheck)
		# Créer une erreur si dans le fichier de liste il y a une ligne vide, urllib bloque
		
		try:
			codeResult = urllib.request.urlopen(urlCheck, timeout=10).getcode()
			print(codeResult)
			# On met en forme le resultat
			result="%s; %s \n" %(urlCheck,codeResult)
			# On ecrit le resultat dans le fichier
			fileWr.write(result)
		except timeout:
			codeResult = "Timeout"
			result = "%s; %s \n" %(urlCheck,codeResult)
			print (codeResult)
			# On ecrit le resultat dans le fichier
			fileWr.write(result)
		except (HTTPError) as url:
			url.code == 404
			codeResult = url.code
			# On met en forme le resultat
			result = "%s; %s \n" %(urlCheck,codeResult)
			print (codeResult)
			# On ecrit le resultat dans le fichier
			fileWr.write(result)
		except (URLError):
			codeResult = "Non conforme : URLError"
			# On met en forme le resultat
			result = "%s; %s \n" %(urlCheck,codeResult)
			print (codeResult)
			# On ecrit le resultat dans le fichier
			fileWr.write(result)
		



##################
### Main
##################


# On vérifie les parametres
checkFile()

# Lecture des URLs
getList()

# On ouvre le fichier de resultats
fileWr = open(fileOut, "w")

# On traite les Urls
testList()

# On ferme le fichier
fileWr.close()

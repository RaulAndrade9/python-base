import sys
import os

#LBYL = Look Before You Leap
#EAFP - Easy to ask forgiveness than permission (mais fácil pedir perdão do que permissão)

try: 
    names = open("names.txt").readlines()
except FileNotFoundError as e: 
    print("[Error] str(e).")
    sys.exit(1)
except AttributeError:
    print("Error: List doesnt have banana")
    sys.exit(1)



try:
    print(names[2])
except:
    print("Error: Missing name in the list")
    sys.exit(1)
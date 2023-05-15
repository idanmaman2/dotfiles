import sys
import pyfiglet 

print('\033[93m',end="")
#banner 
result = pyfiglet.figlet_format("IDHM ;-)\nPYTHON", font = "Doom" )
print(result)
#all the ascii and thier hex 
print(*[",".join((chr(i) , hex(i))) for i in range(32,126)],sep="|")
#change the ps 
sys.ps1="*_*>"
sys.ps2=".__."
print('\033[95m',end="")
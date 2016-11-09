from automatische_uitgaan import *

# automatische_uitschakelen(1)

def uitschakelen(aanknop, automatisch_uitschakelen):
    if aanknop == 1:
        if automatisch_uitschakelen == True:
            return 'Joop'

# uitschakelen(aanknop, automatische_uitschakelen(aanknop))
print(uitschakelen(aanknop, automatische_uitschakelen(aanknop)))

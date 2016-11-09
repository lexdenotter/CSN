import time


def automatische_uitschakelen(aanknop):
    if aanknop == 1:
        nu_tijd= time.strftime('%A %b %d %y %I:%M %p', time.localtime())
        print(nu_tijd)
        tijd_seconden= time.time()
        tijd_later= float(tijd_seconden) + (10)
        print(tijd_later)
        while True:
            if int(tijd_seconden) == int(tijd_later):
                break
            else:
                tijd_seconden= time.time()
                # print(tijd_seconden)
                pass



        print(tijd_seconden)
        print(tijd_later)
        return True

aanknop= 1

# automatische_uitschakelen(aanknop)
#print(automatische_uitschakelen(aanknop))

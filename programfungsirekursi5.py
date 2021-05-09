# konversi bilangan biner ke desimal

def binerKeDesimal(biner):
    pangkat = len(biner)-1
    desimal = 0
    for i in range(len(biner)):
        iBin = int(biner[i])
        iDes = iBin * (2**pangkat)
        desimal += iDes
        pangkat -= 1
    return desimal

def desimalKeBiner(desimal):
    biner = ""
    while(desimal != 0):
        biner = str(desimal % 2) + biner
        desimal //= 2
    return biner

biner = input()

desimal = binerKeDesimal(biner)
hasil = desimalKeBiner(desimal)
print(desimal)
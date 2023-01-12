def nama():
    global nm
    nm = input ('masukkan nama\t\t\t: ')
    return nm

def nim():
    global n
    n = input('masukkan nim\t\t\t: ')
    return n

def tugas():
    global tgs
    tgs = int(input('masukkan nilai tugas\t: '))
    return tgs

def uts():
    global ut
    ut = int(input('masukkan nilai uts\t\t: '))
    return ut

def uas():
    global ua
    ua = int(input('masukkan nilai uas\t\t: '))
    return ua

def akhir():
    global ak
    ak = (0.30*tgs)+(0.35*ut)+(0.35*ua)
    return ak
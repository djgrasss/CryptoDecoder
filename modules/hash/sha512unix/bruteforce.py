from passlib.hash import sha512_crypt

def bf(h, dictionary):

    f = open(dictionary, 'r')
    lines = f.readlines()
    print('\033[1;34m[*]\033[0m Starting Brute Force - hash = ' + h)
    for i in lines:
    
        h2 = sha512_crypt.hash(i[:-1])
    
        if h == h2:
    
            print('\033[1;32m[+]\033[0m Hash Cracked! - Password = ' + i)
    

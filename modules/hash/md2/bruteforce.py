from Crypto.Hash import MD2

def bf(h, dictionary):

    f = open(dictionary, 'r')
    lines = f.readlines()
    print('\033[1;34m[*]\033[0m Starting Brute Force - hash = ' + h)
    for i in lines:
    
        md2hasher = MD2.new()
        md2hasher.update(i[:-1])
        h2 = md2hasher.hexdigest()
    
        if h == h2:
    
            print('\033[1;32m[+]\033[0m Hash Cracked! - Password = ' + i)
            exit()
    

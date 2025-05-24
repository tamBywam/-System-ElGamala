import sys
import random
from math import gcd

def rozszerzony_euklides(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        nwd, y, x = rozszerzony_euklides(b % a, a)
        return (nwd, x - (b // a) * y, y)

def odwrotnosc_modularna(a, m):
    nwd, x, _ = rozszerzony_euklides(a, m)
    if nwd != 1:
        return None
    else:
        return x % m

def wczytaj_parametry_elgamal():
    with open('elgamal.txt', 'r') as plik:
        p = int(plik.readline().strip())
        g = int(plik.readline().strip())
    return p, g

def wygeneruj_klucze():
    p, g = wczytaj_parametry_elgamal()
    prywatny_klucz = random.randint(2, p-2)
    klucz_publiczny = pow(g, prywatny_klucz, p)
    
    with open('private.txt', 'w') as plik:
        plik.write(f"{p}\n{g}\n{prywatny_klucz}\n")
    
    with open('public.txt', 'w') as plik:
        plik.write(f"{p}\n{g}\n{klucz_publiczny}\n")

def wczytaj_klucz_publiczny():
    with open('public.txt', 'r') as plik:
        p = int(plik.readline().strip())
        g = int(plik.readline().strip())
        beta = int(plik.readline().strip())
    return p, g, beta

def wczytaj_klucz_prywatny():
    with open('private.txt', 'r') as plik:
        p = int(plik.readline().strip())
        g = int(plik.readline().strip())
        b = int(plik.readline().strip())
    return p, g, b

def zaszyfruj_wiadomosc():
    p, g, beta = wczytaj_klucz_publiczny()
    
    with open('plain.txt', 'r') as plik:
        m = int(plik.readline().strip())
    
    if m >= p:
        print("Błąd: wiadomość musi być mniejsza od p")
        sys.exit(1)
    
    k = random.randint(2, p-2)
    g_do_k = pow(g, k, p)
    beta_do_k = pow(beta, k, p)
    szyfrogram = (m * beta_do_k) % p
    
    with open('crypto.txt', 'w') as plik:
        plik.write(f"{g_do_k}\n{szyfrogram}\n")

def odszyfruj_wiadomosc():
    p, _, b = wczytaj_klucz_prywatny()
    
    with open('crypto.txt', 'r') as plik:
        g_do_k = int(plik.readline().strip())
        szyfrogram = int(plik.readline().strip())
    
    sekret = pow(g_do_k, b, p)
    odwrotnosc_sekretu = odwrotnosc_modularna(sekret, p)
    odszyfrowana = (szyfrogram * odwrotnosc_sekretu) % p
    
    with open('decrypt.txt', 'w') as plik:
        plik.write(f"{odszyfrowana}\n")

def podpisz_wiadomosc():
    p, g, b = wczytaj_klucz_prywatny()
    
    with open('message.txt', 'r') as plik:
        m = int(plik.readline().strip())
    
    if m >= p:
        print("Błąd: wiadomość musi być mniejsza od p")
        sys.exit(1)
    
    while True:
        k = random.randint(2, p-2)
        if gcd(k, p-1) == 1:
            break
    
    r = pow(g, k, p)
    odwrotnosc_k = odwrotnosc_modularna(k, p-1)
    x = ((m - b * r) * odwrotnosc_k) % (p-1)
    
    with open('signature.txt', 'w') as plik:
        plik.write(f"{r}\n{x}\n")

def zweryfikuj_podpis():
    p, g, beta = wczytaj_klucz_publiczny()
    
    with open('message.txt', 'r') as plik:
        m = int(plik.readline().strip())
    
    with open('signature.txt', 'r') as plik:
        r = int(plik.readline().strip())
        x = int(plik.readline().strip())
    
    lewa_strona = pow(g, m, p)
    prawa_strona = (pow(r, x, p) * pow(beta, r, p)) % p
    
    wynik = 'T' if lewa_strona == prawa_strona else 'N'
    
    print(wynik)
    with open('verify.txt', 'w') as plik:
        plik.write(f"{wynik}\n")

def main():
    if len(sys.argv) != 2:
        print("Użycie: python elgamal.py -k|-e|-d|-s|-v")
        sys.exit(1)
    
    opcja = sys.argv[1]
    
    if opcja == '-k':
        wygeneruj_klucze()
    elif opcja == '-e':
        zaszyfruj_wiadomosc()
    elif opcja == '-d':
        odszyfruj_wiadomosc()
    elif opcja == '-s':
        podpisz_wiadomosc()
    elif opcja == '-v':
        zweryfikuj_podpis()
    else:
        print("Nieprawidłowa opcja")
        sys.exit(1)

if __name__ == "__main__":
    main()

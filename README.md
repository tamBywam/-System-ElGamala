# ElGamal – Szyfrowanie i podpisy cyfrowe

Program `elgamal` implementuje mechanizmy szyfrowania i podpisywania wiadomości na podstawie algorytmu ElGamala. Program korzysta z pliku `elgamal.txt`, który zawiera dwie liczby:

- liczbę pierwszą `p`
- generator `g`

Przykładowa zawartość pliku `elgamal.txt`:
1665997633093155705263923663680487185948531888850484859473375695734301776192932338784530163
170057347237941209366519667629336535698946063913573988287540019819022183488419112350737049

markdown
Copy
Edit

## Sposób użycia

Program uruchamiany jest z jedną z poniższych opcji:

### `-k` — Generowanie kluczy

- Wczytuje dane z pliku `elgamal.txt`.
- Generuje parę kluczy:
  - Klucz prywatny zapisywany do `private.txt`.
  - Klucz publiczny zapisywany do `public.txt`.
- Każdy z plików klucza zawiera:
  1. Liczbę `p`
  2. Generator `g`
  3. Odpowiednio wykładnik (klucz prywatny) lub potęgę (klucz publiczny)

### `-e` — Szyfrowanie wiadomości

- Wczytuje klucz publiczny z `public.txt`.
- Wczytuje wiadomość z pliku `plain.txt`.
- Zapisuje zaszyfrowaną wiadomość do pliku `crypto.txt`.
- Jeśli wiadomość `m ≥ p`, zgłaszany jest błąd.

### `-d` — Odszyfrowywanie wiadomości

- Wczytuje klucz prywatny z `private.txt`.
- Wczytuje kryptogram z `crypto.txt`.
- Zapisuje odszyfrowaną wiadomość do pliku `decrypt.txt`.

### `-s` — Podpisywanie wiadomości

- Wczytuje klucz prywatny z `private.txt`.
- Wczytuje wiadomość z pliku `message.txt`.
- Generuje podpis:
  - Zapisywany do pliku `signature.txt` (dwa wiersze: `r`, `x`).

### `-v` — Weryfikacja podpisu

- Wczytuje klucz publiczny z `public.txt`.
- Wczytuje wiadomość z `message.txt`.
- Wczytuje podpis z `signature.txt`.
- Sprawdza poprawność podpisu.
- Wynik (`T` – poprawny, `N` – niepoprawny) wyświetlany jest na ekranie oraz zapisywany do pliku `verify.txt`.

## Uwagi

- Pliki `plain.txt` i `message.txt` mogą mieć identyczną zawartość.
- Poprawność programu można sprawdzić porównując zawartość `plain.txt` i `decrypt.txt` oraz testując poprawność weryfikacji podpisu (zarówno poprawnego, jak i sfałszowanego).

## Wymagania techniczne

- Program musi obsługiwać liczby kilkusetbitowe.
- W językach takich jak Python obsługa dużych liczb jest natywna.
- W językach takich jak Java wymagane będzie użycie odpowiednich bibliotek (np. `BigInteger`).

## Ograniczenia

Program **nie ma prawa odczytywać innych plików** niż wskazane dla danej opcji działania.
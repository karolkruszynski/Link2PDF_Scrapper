# PDF Crawler

PDF Crawler to prosty skrypt w Pythonie, który wyszukuje pliki PDF w wynikach wyszukiwania Google dla podanej frazy. Zebrane linki do plików PDF są zapisywane w pliku Excel.

## Wymagania

- Python 3.7 lub nowszy
- Biblioteki:
  - `playwright`
  - `requests`
  - `openpyxl`

## Instalacja

1. **Klonowanie repozytorium**

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
   
## Tworzenie wirtualnego środowiska (opcjonalnie)

 ```bash
python -m venv venv
source venv/bin/activate  # na Linux/Mac
venv\Scripts\activate  # na Windows
```

## Instalacja wymaganych bibliotek
```bash
pip install playwright requests openpyxl
playwright install
```

## Użycie
1. Edytuj skrypt main.py, aby zmienić zapytanie w zmiennej query:

 ```bash
query = 'filetype:pdf site:www.lexington.com'
```
2. Uruchom skrypt
```bash
python main.py
```
3. Wyniki:
Linki do plików PDF zostaną zapisane w pliku pdf_links.xlsx.

## Jak to działa?
Skrypt otwiera stronę Google w trybie incognito.
Wysyła zapytanie do Google w formacie filetype:pdf site:<adres_strony>.
Zbiera linki do plików PDF z wyników wyszukiwania.
Sprawdza, czy linki prowadzą do rzeczywistych plików PDF.
Zapisuje zebrane linki do pliku Excel.

## Uwagi
Upewnij się, że masz zainstalowaną przeglądarkę Chromium lub inną zgodną z Playwright.
Możesz dostosować parametry, takie jak czas oczekiwania między zapytaniami, aby poprawić skuteczność skryptu.

## Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT.



import os
import requests
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import openpyxl


# Funkcja do sprawdzania, czy link prowadzi do pliku PDF
def is_pdf(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.headers.get('Content-Type') == 'application/pdf'
    except requests.RequestException:
        return False


# Funkcja do zapisywania linków PDF do pliku Excel
def save_links_to_excel(pdf_links, filename="pdf_links.xlsx"):
    # Tworzymy nowy skoroszyt Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "PDF Links"

    # Nagłówki kolumn
    sheet.append(["Nazwa pliku", "Link"])

    # Dodawanie linków do PDF do pliku Excel
    for link in pdf_links:
        # Wyciągnięcie nazwy pliku z linku
        file_name = link.split("/")[-1] # Odwrócenie stringa a następnie split
        sheet.append([file_name, link])

    # Zapisujemy do pliku
    workbook.save(filename)
    print(f"Zapisano linki do pliku: {filename}")


# Playwright - wyszukiwanie PDF-ów i zapisywanie linków
def search_and_save_pdfs():
    query = 'filetype:pdf site:www.lexington.com'

    with sync_playwright() as p:
        # Uruchomienie przeglądarki
        browser = p.chromium.launch(headless=True)  # headless=True, jeśli chcesz w trybie bez okna
        # Utworzenie nowego kontekstu w trybie incognito
        context = browser.new_context()

        # Otwórz nową stronę w kontekście incognito
        page = context.new_page()

        # Wejdź na stronę Google
        page.goto("https://www.google.com")
        page.wait_for_timeout(5000)

        # Tworzymy URL z zapytaniem
        url = f"https://www.google.com/search?q={query}"

        # Przejdź do URL z wynikami wyszukiwania
        page.goto(url)

        # Czekaj na wyniki wyszukiwania
        page.wait_for_selector('a')

        pdf_links = []

        while True:
            # Pobierz wszystkie linki do PDF-ów z wyników wyszukiwania
            for link in page.query_selector_all('a'):
                href = link.get_attribute('href')
                if href and "pdf" in href:
                    full_url = urljoin(page.url, href)
                    if is_pdf(full_url):  # Weryfikacja linku PDF
                        pdf_links.append(full_url)

            print(f"Znaleziono {len(pdf_links)} linków do plików PDF na tej stronie.")

            # Sprawdzenie, czy istnieje przycisk "Next"
            next_button = page.query_selector('#pnnext')
            if next_button:
                next_button.click()
                page.wait_for_timeout(2000)  # Czekaj na załadowanie kolejnej strony
                page.wait_for_selector('a')  # Czekaj na nowe linki
            else:
                break  # Wyjdź z pętli, jeśli przycisk "Next" nie istnieje

        # Zapisz linki do pliku Excel
        save_links_to_excel(pdf_links)

        # Zamknij przeglądarkę
        browser.close()


# Uruchom funkcję
if __name__ == "__main__":
    search_and_save_pdfs()

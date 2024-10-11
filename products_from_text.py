import re


def extract_products(text):
    # Wyrażenie regularne do ekstrakcji SKU, nazwy i wymiarów (uwzględnia więcej formatów)
    pattern = r'(\d{4}-\d{3,4}[A-Za-z0-9]*)\s+(.*?)\s+(\d{1,2}W\s+x\s+\d{1,2}D\s+x\s+\d{1,2}(?:\.?\d*)?H\s+in\.|\d{1,2}\s+diameter\s+x\s+\d{1,2}(?:\.?\d*)?H\s+in\.)'

    matches = re.findall(pattern, text, re.DOTALL)  # re.DOTALL, aby uwzględnić wielolinijkowe teksty

    # Przechowywanie wyników w liście słowników
    products = []
    for match in matches:
        product = {
            "SKU": match[0],
            "Name": match[1].strip(),
            "Dimensions": match[2].strip()
        }
        products.append(product)

    return products


# Przykładowy tekst
text = """
2055-973 Credo Hall Chest
38W x 18D x 36.75H in.
Shown on pages: 98 and 99

2064-951 Sulu Sea Snake 
Rectangular Spot Table
20W x 12D x 22H in.
Shown on page: 254

2077-950C Precept Round End Table
26 diameter x 24H in.
Shown on pages: 220 and 221

2080-951 Greta Large Round Spot Table
18 diameter x 23.5H in.
Shown on pages: 204 and 205

2097-957 Zephyr Square End Table
25W x 25D x 25H in.
Shown on page: 206

2087-880-01 Melody Side Chair
Standard fabric 153711 
2087-880 Melody Side Chair
Lexington fabrics and leathers and COM 
22W x 24.75D x 37.5H in.
Shown on pages: 20, 22, 25, 27 and 274

2060-945 Impresario Rectangular Cocktail
54.25W x 33D x 17.75H in.
Shown on pages: 156 and 157

2066-955 Corrina Spot Table
18W x 12D x 20H in.
Shown on page: 253

2077-957C Precept Square End Table
25W x 25D x 24H in.
Shown on page: 223
"""

# Wywołanie funkcji
extracted_products = extract_products(text)

# Wyświetlenie wyników
for product in extracted_products:
    print(f"SKU: {product['SKU']}")
    print(f"Name: {product['Name']}")
    print(f"Dimensions: {product['Dimensions']}\n")

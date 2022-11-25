import re

pattern = r"(@[#]+)([A-Z]([a-zA-Z0-9]{4,})[A-Z])(@[#]+)"
digits_group = r"(\d+)"

number_barcodes = int(input())

for barcodes in range(number_barcodes):
    digits_product_group = '00'
    barcode = input()
    fancy_barcode = re.findall(pattern, barcode)
    if fancy_barcode:
        numbers_in_barcode = fancy_barcode[0][1]
        product_group = re.findall(digits_group, numbers_in_barcode)
        if product_group:
            digits_product_group = ''.join(product_group)
        print(f"Product group: {digits_product_group}")
    else:
        print("Invalid barcode")
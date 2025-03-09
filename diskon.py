def hitung_total_bayar(belanja):
    if belanja > 100000:
        diskon = 0.10
    elif belanja > 50000:
        diskon = 0.05
    else:
        diskon = 0.0

    total_diskon = belanja * diskon
    total_bayar = belanja - total_diskon

    return total_bayar

belanja = float(input("Masukan total belanja: "))
total_bayar = hitung_total_bayar(belanja)
print(f"Total yang harus dibayar setelah diskon: {total_bayar}")
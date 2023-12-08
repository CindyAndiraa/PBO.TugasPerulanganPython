# Program menggunakan for loop
total = 0

for i in range(1, 6):  # Loop dari 1 sampai 5
    if i % 2 == 0:  # Jika i adalah bilangan genap
        total += i
    else:  # Jika i adalah bilangan ganjil
        total -= i

print("Total dengan For Loop:", total)
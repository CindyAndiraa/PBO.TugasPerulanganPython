# Program menggunakan while loop
counter = 1
sum_even = 0
sum_odd = 0

while counter <= 5:
    if counter % 2 == 0:
        sum_even += counter
    else:
        sum_odd += counter
    counter += 1

print("Total bilangan genap dengan While Loop:", sum_even)
print("Total bilangan ganjil dengan While Loop:", sum_odd)
# *Tugas 1 Pemrograman Perbasis Objek*
## Nama : Cindy Andira
## NPM  : G1F022059

## 1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut:(https://github.com/randiijulian/randiijulian/assets/81604461/e32b6d92-7e3a-4323-a0e3-711009112c8e)
- **Source Code** :  
```
for i in range(1, 101):
    if i % 10 == 0:
        print("Cindy Andira\nCindy Andira\nCindy Andira")
    else:
        print(i)
```
 - **Output :** 

1
2
3
4
5
6
7
8
9
Cindy Andira
Cindy Andira
Cindy Andira
11
12
13
14
15
16
17
18
19
Cindy Andira
Cindy Andira
Cindy Andira
21
22
23
24
25
26
27
28
29
Cindy Andira
Cindy Andira
Cindy Andira
31
32
33
34
35
36
37
38
39
Cindy Andira
Cindy Andira
Cindy Andira
41
42
43
44
45
46
47
48
49
Cindy Andira
Cindy Andira
Cindy Andira
51
52
53
54
55
56
57
58
59
Cindy Andira
Cindy Andira
Cindy Andira
61
62
63
64
65
66
67
68
69
Cindy Andira
Cindy Andira
Cindy Andira
71
72
73
75
76
78
79
Cindy Andira
Cindy Andira
81
82
83
84
85
86
87
88
89
Cindy Andira
Cindy Andira
Cindy Andira
91
92
93
94
95
96
97
98
99
Cindy Andira
Cindy Andira
Cindy Andira

 - **Penjelasan :** 

Code tersebut menggunakan loop `for` untuk mengiterasi nilai dari 1 hingga 100. Pada setiap iterasi, dijalankan pernyataan kondisional `if-else`. Jika nilai `i` habis dibagi 10 (`i % 10 == 0`), maka akan mencetak "Cindy Andira" sebanyak tiga kali. Jika tidak, maka akan mencetak nilai `i` itu sendiri.

Jadi, setiap kali `i` adalah kelipatan 10 (10, 20, 30, ..., 100), pesan "Cindy Andira" akan dicetak tiga kali, dan untuk nilai `i` lainnya, nilai `i` itu sendiri akan dicetak.

## 2 Buatlah program bebas, dengan menerapkan if else pada: a. For Loops b. While Loops
***a. For Loops***

 - **Source Code :** 
```
# Program menggunakan for loop
total = 0

for i in range(1, 6):  # Loop dari 1 sampai 5
    if i % 2 == 0:  # Jika i adalah bilangan genap
        total += i
    else:  # Jika i adalah bilangan ganjil
        total -= i

print("Total dengan For Loop:", total)
```

 - **Output :**
 Total dengan For Loop: -3

 - **Penjelasan :**
Code tersebut adalah program Python yang menggunakan loop `for` untuk menghitung total dari deret bilangan. Mari jelaskan langkah-langkahnya:

1. `total` diinisialisasi dengan nilai 0.
2. `for i in range(1, 6):` membuat loop yang berjalan untuk nilai `i` dari 1 hingga 5 (inklusif).
3. Pada setiap iterasi, ada kondisi `if i % 2 == 0:`. Ini mengecek apakah `i` adalah bilangan genap.
4. Jika `i` adalah bilangan genap, nilai `i` ditambahkan ke `total`.
5. Jika `i` adalah bilangan ganjil, nilai `i` dikurangkan dari `total`.
6. Setelah loop selesai, nilai total dicetak.

Contoh:
- Iterasi pertama (i = 1): `1` adalah ganjil, sehingga `total = 0 - 1 = -1`.
- Iterasi kedua (i = 2): `2` adalah genap, sehingga `total = -1 + 2 = 1`.
- Iterasi ketiga (i = 3): `3` adalah ganjil, sehingga `total = 1 - 3 = -2`.
- Iterasi keempat (i = 4): `4` adalah genap, sehingga `total = -2 + 4 = 2`.
- Iterasi kelima (i = 5): `5` adalah ganjil, sehingga `total = 2 - 5 = -3`.

Hasil akhirnya dicetak, dan output yang dihasilkan oleh program adalah "Total dengan For Loop: -3".


***b. while Loops***

- **Source Code :**
```
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
```

- **Output :** 
Total bilangan genap dengan While Loop: 6
Total bilangan ganjil dengan While Loop: 9

- **Penjelasan :**

Code tersebut adalah program Python yang menggunakan loop `while` untuk menghitung total dari bilangan genap dan ganjil. Mari jelaskan langkah-langkahnya:

1. Variabel `counter` diinisialisasi dengan nilai 1.
2. Variabel `sum_even` dan `sum_odd` diinisialisasi dengan nilai 0. Ini digunakan untuk menyimpan total bilangan genap dan ganjil.
3. `while counter <= 5:` membuat loop yang akan berjalan selama nilai `counter` kurang dari atau sama dengan 5.
4. Di dalam loop, ada kondisi `if counter % 2 == 0:`. Ini mengecek apakah `counter` adalah bilangan genap.
5. Jika `counter` adalah bilangan genap, maka nilai `counter` ditambahkan ke `sum_even`.
6. Jika `counter` adalah bilangan ganjil, maka nilai `counter` ditambahkan ke `sum_odd`.
7. `counter` ditambah 1 pada setiap iterasi untuk menghindari infinite loop.
8. Setelah loop selesai, total bilangan genap dan ganjil dicetak.

Contoh:
- Iterasi pertama (counter = 1): `1` adalah ganjil, sehingga `sum_odd = 0 + 1 = 1`.
- Iterasi kedua (counter = 2): `2` adalah genap, sehingga `sum_even = 0 + 2 = 2`.
- Iterasi ketiga (counter = 3): `3` adalah ganjil, sehingga `sum_odd = 1 + 3 = 4`.
- Iterasi keempat (counter = 4): `4` adalah genap, sehingga `sum_even = 2 + 4 = 6`.
- Iterasi kelima (counter = 5): `5` adalah ganjil, sehingga `sum_odd = 4 + 5 = 9`.

Hasil akhirnya dicetak, dan output yang dihasilkan oleh program adalah "Total bilangan genap dengan While Loop: 6" dan "Total bilangan ganjil dengan While Loop: 9".

## 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for

- **Source Code :**
```
# Mendefinisikan array (list) dengan beberapa nilai
my_array = [10, 20, 30, 40, 50]

# Menampilkan semua nilai dalam array menggunakan perulangan for
print("Isi array:")
for value in my_array:
    print(value)
```

- **Output :**
Isi array:
10
20
30
40
50

- **Penjelasan :**

Code tersebut adalah program Python yang mendefinisikan sebuah array (list) dengan beberapa nilai dan kemudian menampilkan semua nilai dalam array tersebut menggunakan perulangan `for`. Mari kita jelaskan langkah-langkahnya:

1. `my_array` adalah variabel yang menyimpan sebuah list `[10, 20, 30, 40, 50]`.
2. Perulangan `for value in my_array:` digunakan untuk mengiterasi setiap nilai dalam list `my_array`.
3. Pada setiap iterasi, nilai dari list (dalam hal ini disimpan dalam variabel `value`) dicetak menggunakan pernyataan `print(value)`.
4. Program mencetak pesan "Isi array:" sebelum mencetak setiap nilai dalam array.

Contoh output:
```
Isi array:
10
20
30
40
50
```

Output ini menunjukkan nilai-nilai dalam array secara berurutan. Anda dapat mengganti nilai dalam array atau menambahkan/menghapus elemen sesuai kebutuhan Anda.
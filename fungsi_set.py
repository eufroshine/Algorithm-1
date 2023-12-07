# Empty Set Creation and Type Printing
s = set()
print("Type of s is ", type(s))

# Deklarasi List
lis1 = [3, 4, 1, 4, 5]

# Cetak Iterasi sebelum Konversi
print("The list before conversion is: " + str(lis1))

# Iterables setelah konversi
set_from_list = set(lis1)
print("The list after conversion is: " + str(set_from_list))

# set() pada tuple
# deklarasi tuple
tup1 = (3, 4, 1, 4, 5)

# cetak iterasi sebelum konversi
print("The tuple before conversion is: " + str(tup1))

# Iterables after conversion are
# notice distinct and elements
set_from_tuple = set(tup1)
print("The tuple after conversion is: " + str(set_from_tuple))

# fungsi set() pada range
# deklarasi range
r = range(5)
set_from_range = set(r)
print("The Range after conversion is: " + str(set_from_range))

# fungsi set() pada kamus
# deklarasi dictionary
dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}

# cetak dictionary
# internal sorted
print("Dictionary before conversion is: " + str(dic1))
# kamus setelah konfersi
set_from_dict = set(dic1.keys())
print("Dictionary keys after conversion is: " + str(set_from_dict))

# Hapus Elemen dari Set menggunakan Metode pop()
def Remove(initial_set):
    while initial_set:
        initial_set.pop()
    print("Set after popping elements:", initial_set)

initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)

# ===========================================

s1 = {1, 2, 3, 4}
print("Before popping: ", s1)
s1.pop()
s1.pop()
s1.pop()
print("After 3 elements popped, s1:", s1)

# Setel Metode pop() dengan Python
s1 = {9, 1, 0}
popped_element = s1.pop()
print("Popped element:", popped_element)
print("Set after popping one element:", s1)

# Bagaimana Python mengatur issubset() Bekerja
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print("A is subset of B:", A.issubset(B))
print("B is subset of A:", B.issubset(A))

# Contoh Metode set issubset() Python
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print("s2 is subset of s1:", s2.issubset(s1))

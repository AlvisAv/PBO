# Langkah 4
print('ini teks dari modul')

# Langkah 5
print(__name__)

# Langkah 6 
if __name__ == "__main__":
    print('Anda menjalankan module.py')
else:
    print('Anda mengimport modul')

# Langkah 7
counter = 0

# Langkah 8
def jumlahkan (list):
    hasiljml = 0
    for element in list:
        hasiljml += element
    return hasiljml
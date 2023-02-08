diamond = int(input("Masukkan Angka: "))

for i in range(diamond):
  print(' ' * (diamond-i), end='')
  print('* ' * (i+1))
   
for i in range(1,diamond):
  print(' ' * (i+1), end='')
  print('* ' * (diamond-i))

print()
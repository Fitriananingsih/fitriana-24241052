# percabangan bersarang

# kalkulator
# =,-.x,mod,//,pangkat(exppone)

print(20*"=")
print("kalkulator sederhana")
print(*"=")

angka_1 = float(input("masukkan bilangan 1 ="))
operator = input("operator (+,-,*,/,%,//,**:)=") 
angka_2 = float(input("masukkan bilangan 2 ="))

# percabangan bersarang (elif statement)

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah =(hasil)')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah ={hasil}')
elif operator == 'x' or operator == '*':
    hasil = angka_1 *  angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '%' or operator == 'mod':
    hasil = angka_1 % angka_2
    print(f'hasilnya adalah ={hasil}')
elif operator == '//': 
    hasil = angka_1 // angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '**' : 
    hasil = angka_1 ** angka_2 
    print (f'hasilnya adalah = "{hasil}')
else: 
    print (f'operator{operator} tidak ditemukan')

    print ("terima kasih")
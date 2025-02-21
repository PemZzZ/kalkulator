def kalkulator():
    print("\n kalkulator sederhana")
    print("====================================")
    print("pilih operasi:")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("====================================")
    
    while True:
        try:
            pilihan = int(input("masukkan pilihan (1/2/3/4): "))
            if pilihan not in (1,2,3,4):
                print("pilihan tidak valid, coba lagi")
                continue
            
            angka1 = float(input("masukan angka pertama:"))
            angka2 = float(input("masukan angka kedua:"))
            
            if pilihan == 1:
                hasil = angka1 + angka2
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == 2:
                hasil = angka1 - angka2
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == 3:
                hasil = angka1 * angka2
                print(f"Hasil: {angka1} X {angka2} = {hasil}")
            elif pilihan == 4:
                if angka2 == 0:
                 print("ga bisa di bagi 0 dong woi!!!")
                hasil = angka1 / angka2
                print(F"Hasil: {angka1} / {angka2} = {hasil}")
        
        except ValueError:
            print("input tidak valid")
            continue
        
        lanjut = input("masih lanjut? (y/n) ").lower()
        print("====================================")
        print(" ")
        if lanjut != 'y':
         print("makasih ya udah make")
         break
    
            
            

kalkulator()
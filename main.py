### Project Kalkulator sederhana bangun dan raung

# membuat kalkulator bangun dan ruang secara otomatis
# menampilkan hasil yang diinginkan beserta rumus dan pemecahan nya
# LET'S START

# memasukkan jenis benda yang ingin dihitung
input_jenis = input("Masukkan jenis bangun : ")
jenis = input_jenis.lower()

# tentukan rumus yang akan digunakan sesuai input yang dimasukkan

# 1. Persegi
if jenis == "persegi":
    nama = "PERSEGI"
    sisi1 = float(input("Masukkan sisi : "))
    luas = sisi1 ** 2
    keliling = 4 * sisi1
    print("\n",10*'=',nama,10*'=',"\n")
    rumus_luas="sisi x sisi"
    rumus_keliling="4 x sisi"
    print(f"""
Sisi {nama} yang anda masukkan = {sisi1}
Rumus luas {nama} adalah {rumus_luas} ,
dan rumus keliling {nama} adalah {rumus_keliling}
{20*'='}

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = {sisi1} x {sisi1} = {luas}
{10*'='}
Keliling {nama} = {keliling}
dengan perhitungan = 4 x {sisi1} = {keliling}
    """)

# 2.Persegi Panjang
elif jenis == "persegi panjang":
    nama = "PERSEGI PANJANG"
    sisi1 = float(input("Masukkan panjang : "))
    sisi2 = float(input("Masukkan lebar : "))
    luas = sisi1 * sisi2
    keliling = (2*sisi1) + (2*sisi2)
    print("\n",10*'=',nama,10*'=',"\n")
    rumus_luas="panjang x lebar"
    rumus_keliling="(2 x panjang) + (2 x lebar)\nATAU\n2(panjang + lebar)"
    print(f"""
Panjang yang anda masukkan = {sisi1}
Lebar yang anda masukkan = {sisi2}

Rumus luas {nama} adalah {rumus_luas} ,
dan rumus keliling {nama} adalah {rumus_keliling}
{20*'='}

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = {sisi1} x {sisi2}= {luas}
{10*'='}
Keliling {nama} = {keliling}
dengan perhitungan = 2({sisi1} + {sisi2}) = {keliling}
    """)

# 3.Segitiga
elif jenis == "segitiga":
    nama = "segitiga"
    input_operasi= input("Luas atau Keliling? : ")
    operasi=input_operasi.lower()
    if operasi == "luas":
    
        sisi1 = float(input("Masukkan Alas : "))
        sisi2 = float(input("Masukkan Tinggi : "))

        luas = (sisi1 * sisi2) / 2
        rumus_luas="Alas x Tinggi : 2"
        
        print("\n",10*'=',nama,10*'=',"\n")

        print(f"""
    Alas yang anda masukkan = {sisi1}
    Tinggi yang anda masukkan = {sisi2}
    
    Rumus luas {nama} adalah = {rumus_luas} ,

    Jadi,
    Luas {nama} = {luas} 
    dengan perhitungan = {sisi1} x {sisi2} : 2 = {luas}
    {10*'='}
    
        """)
    elif operasi == "keliling":
    
        sisi1 = float(input("Masukkan Sisi 1 : "))
        sisi2 = float(input("Masukkan Sisi 2 : "))
        sisi3 = float(input("Masukkan Sisi 3 : "))

        
        keliling = sisi1 + sisi2 + sisi3
        print("\n",10*'=',nama,10*'=',"\n")
    
    
        rumus_keliling="Sisi 1 + Sisi 2 + Sisi 3"
        print(f"""
    Sisi 1 yang anda masukkan = {sisi1}
    Sisi 2 yang anda masukkan = {sisi2}
    Sisi 3 yang anda masukkan = {sisi3}

    rumus keliling {nama} adalah {rumus_keliling}
    {20*'='}

    Jadi,

    Keliling {nama} = {keliling}
    dengan perhitungan = {sisi1} + {sisi2} + {sisi3} = {keliling}
        """)


# 3.Jajar Genjang
elif jenis == "jajar genjang":
    nama = "Jajar Genjang"
    input_operasi= input("Luas atau Keliling? : ")
    operasi=input_operasi.lower()
    if operasi == "luas":
    
        sisi1 = float(input("Masukkan Alas : "))
        sisi2 = float(input("Masukkan Tinggi : "))

        luas = sisi1 * sisi2
        rumus_luas="Alas x Tinggi "
        
        print("\n",10*'=',nama,10*'=',"\n")

        print(f"""
    Alas yang anda masukkan = {sisi1}
    Tinggi yang anda masukkan = {sisi2}
    
    Rumus luas {nama} adalah = {rumus_luas} ,

    Jadi,
    Luas {nama} = {luas} 
    dengan perhitungan = {sisi1} x {sisi2} = {luas}
    {10*'='}
    
        """)
    elif operasi == "keliling":
    
        sisi1 = float(input("Masukkan Sisi 1 : "))
        sisi2 = float(input("Masukkan Sisi 2 : "))
        sisi3 = float(input("Masukkan Sisi 3 : "))
        sisi4 = float(input("Masukkan Sisi 4 : "))
        
        
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        print("\n",10*'=',nama,10*'=',"\n")
    
    
        rumus_keliling="Sisi 1 + Sisi 2 + Sisi 3"
        print(f"""
    Sisi 1 yang anda masukkan = {sisi1}
    Sisi 2 yang anda masukkan = {sisi2}
    Sisi 3 yang anda masukkan = {sisi3}
    Sisi 4 yang anda masukkan = {sisi4}

    rumus keliling {nama} adalah {rumus_keliling}
    {20*'='}

    Jadi,

    Keliling {nama} = {keliling}
    dengan perhitungan = {sisi1} + {sisi2} + {sisi3} + {sisi4} = {keliling}
        """)

# 4.Trapesium
elif jenis == "trapesium":


    nama = "Trapesium"
    input_operasi= input("Luas atau Keliling? : ")
    operasi=input_operasi.lower()
    if operasi == "luas":
    
        sisi1 = float(input("Masukkan sisi 1 : "))
        sisi2 = float(input("Masukkan sisi 2 : "))
        sisi3 = float(input("Masukkan tinggi : "))

        luas = ((sisi1 + sisi2)*sisi3)/2
        rumus_luas="(sisi pertama + sisi kedua) x tinggi : 2"
        
        print("\n",10*'=',nama,10*'=',"\n")

        print(f"""
Sisi 1 yang anda masukkan = {sisi1}
Sisi 2 yang anda masukkan = {sisi2}
Tinggi yang anda masukkan = {sisi3}
    
Rumus luas {nama} adalah = {rumus_luas} ,

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = ({sisi1} + {sisi2}) x {sisi3} : 2 = {luas}
{10*'='}
    
        """)
    elif operasi == "keliling":
    
        sisi1 = float(input("Masukkan Sisi 1 : "))
        sisi2 = float(input("Masukkan Sisi 2 : "))
        sisi3 = float(input("Masukkan Sisi 3 : "))
        sisi4 = float(input("Masukkan Sisi 4 : "))
        
        
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        print("\n",10*'=',nama,10*'=',"\n")
    
    
        rumus_keliling="Sisi 1 + Sisi 2 + Sisi 3"
        print(f"""
    Sisi 1 yang anda masukkan = {sisi1}
    Sisi 2 yang anda masukkan = {sisi2}
    Sisi 3 yang anda masukkan = {sisi3}
    Sisi 4 yang anda masukkan = {sisi4}

    rumus keliling {nama} adalah {rumus_keliling}
    {20*'='}

    Jadi,

    Keliling {nama} = {keliling}
    dengan perhitungan = {sisi1} + {sisi2} + {sisi3} + {sisi4} = {keliling}
        """)

# 5.Layang-Layang
elif jenis == "layang layang":


    nama = "Layang layang"
    input_operasi= input("Luas atau Keliling? : ")
    operasi=input_operasi.lower()
    if operasi == "luas":
    
        sisi1 = float(input("Masukkan diagonal 1 : "))
        sisi2 = float(input("Masukkan diagonal 2 : "))

        luas = (sisi1 * sisi2)/2
        rumus_luas="(Diagonal 1 x Diagonal 2) : 2"
        
        print("\n",10*'=',nama,10*'=',"\n")

        print(f"""
Diagonal 1 yang anda masukkan = {sisi1}
Diagonal 2 yang anda masukkan = {sisi2}

    
Rumus luas {nama} adalah = {rumus_luas} ,

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = ({sisi1} x {sisi2}) : 2 = {luas}
{10*'='}
    
        """)
    elif operasi == "keliling":
    
        sisi1 = float(input("Masukkan Sisi 1 : "))
        sisi2 = float(input("Masukkan Sisi 2 : "))
        sisi3 = float(input("Masukkan Sisi 3 : "))
        sisi4 = float(input("Masukkan Sisi 4 : "))
        
        
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        print("\n",10*'=',nama,10*'=',"\n")
    
    
        rumus_keliling="Sisi 1 + Sisi 2 + Sisi 3"
        print(f"""
    Sisi 1 yang anda masukkan = {sisi1}
    Sisi 2 yang anda masukkan = {sisi2}
    Sisi 3 yang anda masukkan = {sisi3}
    Sisi 4 yang anda masukkan = {sisi4}

    rumus keliling {nama} adalah {rumus_keliling}
    {20*'='}

    Jadi,

    Keliling {nama} = {keliling}
    dengan perhitungan = {sisi1} + {sisi2} + {sisi3} + {sisi4} = {keliling}
        """)

# 6. Belah Ketupat
elif jenis == "belah ketupat":

    nama = "Layang layang"
    input_operasi= input("Luas atau Keliling? : ")
    operasi=input_operasi.lower()
    if operasi == "luas":
    
        sisi1 = float(input("Masukkan diagonal 1 : "))
        sisi2 = float(input("Masukkan diagonal 2 : "))

        luas = (sisi1 * sisi2)/2
        rumus_luas="(Diagonal 1 x Diagonal 2) : 2"
        
        print("\n",10*'=',nama,10*'=',"\n")

        print(f"""
Diagonal 1 yang anda masukkan = {sisi1}
Diagonal 2 yang anda masukkan = {sisi2}

    
Rumus luas {nama} adalah = {rumus_luas} ,

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = ({sisi1} x {sisi2}) : 2 = {luas}
{10*'='}
    
        """)
    elif operasi == "keliling":
    
        sisi1 = float(input("Masukkan Sisi 1 : "))
        sisi2 = float(input("Masukkan Sisi 2 : "))
        sisi3 = float(input("Masukkan Sisi 3 : "))
        sisi4 = float(input("Masukkan Sisi 4 : "))
        
        
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        print("\n",10*'=',nama,10*'=',"\n")
    
    
        rumus_keliling="Sisi 1 + Sisi 2 + Sisi 3"
        print(f"""
    Sisi 1 yang anda masukkan = {sisi1}
    Sisi 2 yang anda masukkan = {sisi2}
    Sisi 3 yang anda masukkan = {sisi3}
    Sisi 4 yang anda masukkan = {sisi4}

    rumus keliling {nama} adalah {rumus_keliling}
    {20*'='}

    Jadi,

    Keliling {nama} = {keliling}
    dengan perhitungan = {sisi1} + {sisi2} + {sisi3} + {sisi4} = {keliling}
        """)


# 7. Lingkaran
elif jenis == "lingkaran" or " lingkaran " or " lingkaran" or "lingkaran ":
    nama = "Lingkaran"
    sisi1 = float(input("Masukkan jari-jari (r) : "))
    
    if sisi1 %7 == 0:
        phi = "22/7"
        luas = 22/7 * sisi1 * sisi1
        keliling = 2*22/7*sisi1
        print("\n",10*'=',nama,10*'=',"\n")
        rumus_luas="phi x r x r"
        rumus_keliling="2 x Phi x R"
        print(f"""
Jari-jari yang anda masukkan = {sisi1}


Rumus luas {nama} adalah {rumus_luas} ,
dan rumus keliling {nama} adalah {rumus_keliling}
{20*'='}

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = {phi} x {sisi1} x {sisi1} = {int(luas)}
{10*'='}
Keliling {nama} = {keliling}
dengan perhitungan = 2 x {phi} x {sisi1} = {int(keliling)}
        """)

    elif sisi1%7 !=0:
        
        luas = 3.14 * (sisi1 * sisi1)
        keliling = 2*3.14*sisi1
        print("\n",10*'=',nama,10*'=',"\n")
        rumus_luas="phi x r x r"
        rumus_keliling="2 x Phi x R"
        print(f"""
Jari-jari yang anda masukkan = {sisi1}


Rumus luas {nama} adalah {rumus_luas} ,
dan rumus keliling {nama} adalah {rumus_keliling}
{20*'='}

Jadi,
Luas {nama} = {luas} 
dengan perhitungan = 3.14 x {sisi1} x {sisi1} = {luas:.2f}
{10*'='}
Keliling {nama} = {keliling}
dengan perhitungan = 2 x 3.14 x {sisi1} = {keliling:.2f}
        """) 
else:
    print("Bangun yang anda masukkan salah.")

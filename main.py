def main():

    import os
    import sys
    import time

    # Menu
    ans = True
    print("""
        1. Celcius
        2. Reamur
        3. Fahrenheit
        4. Kelvin
        5. Exit """)
    ans = input("Pilih temperatur yang mau di konversi >> ")

    # Celcius
    if ans == '1':
        ans1 = True
        print("""
        1. Reamur
        2. Fahrenheit
        3. Kelvin
        4. Back""")

        ans1 = input("Silahkan masukkan konversi >> ")
        if ans1 == "1":
            data1 = float(input("Masukkan celicius : "))
            result1 = 4 * data1 / 5
            print("Hasil reamur anda adalah ", result1)
            ans2 = True
            ans2 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans2 == "y":
                main()
            elif ans2 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans1 == "2":
            data2 = float(input("Masukkan Celcius : "))
            result2 = 9 * data2 / 5 + 32
            print("Hasil Fahrenheit anda adalah ", result2)
            ans3 = True
            ans3 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans3 == "y":
                main()
            elif ans3 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans1 == "3":
            data3 = float(input("Masukkan Celcius : "))
            result3 = data3 + 273
            print("Hasil Kelvin anda adalah ", result3)
            ans4 = True
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans1 == "4":
            main()

    #Reamur
    elif ans == '2':
        ans5 = True
        print("""
        1. Celcius
        2. Fahrenheit
        3. Kelvin
        4. Back""")
        ans5 = input("Silahkan masukkan konversi >> ")
        if ans5 == "1":
            data4 = float(input("Masukkan Reamur : "))
            result4 = 5 * data4 / 4
            print("Hasil Celcius anda adalah ", result4)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans5 == "2":
            data5 = float(input("Masukkan Reamur : "))
            result5 = 9 * data5 / 4 + 32
            print("Hasil Fahrenheit anda adalah ", result5)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
            data6 = float(input("Masukkan Reamur : "))
            result6 = 5 * data6 / 4 + 273
            print("Hasil Kelvin anda adalah ", result6)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans5 == "4":
            main()

    #Fahrenheit
    elif ans == '3':
        ans6 = True
        print("""
        1. Celcius
        2. Reamur
        3. Kelvin
        4. Back""")
        ans6 = input("Silahkan masukkan konversi >> ")
        if ans6 == "1":
            data7 = float(input("Masukkan Fahrenheit : "))
            result7 = (data7 - 32) * 5 / 9
            print("Hasil Celcius anda adalah ", result7)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans6 == "2":
            data8 = float(input("Masukkan Fahrenheit : "))
            result8 = (data8 - 32) * 4 / 9
            print("Hasil Reamur anda adalah ", result8)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans6 == "3":
            print("STOPPP Gada rumus untuk konversi fahrenheit dengan kelvin. SIlahkan kembali")
            time.sleep(2)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans6 == "4":
            main()


    #Kelvin
    elif ans == '4':
        ans7 = True
        print("""
        1. Celcius
        2. Reamur
        3. Fahrenheit
        4. Back""")
        ans7 = input("Silahkan masukkan konversi >> ")
        if ans7 == "1":
            data9 = float(input("Masukkan Kelvin : "))
            result9 = (data9 - 273)
            print("Hasil Celcius anda adalah ", result9)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans7 == "2":
            data10 = float(input("Masukkan Kelvin : "))
            result10 = (data10 - 273) * 4 / 5
            print("Hasil Reamur anda adalah ", result10)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans7 == "3":
            print("STOPPP Gada rumus untuk konversi Kelvin dengan Fahrenheit. SIlahkan kembali")
            time.sleep(2)
            ans4 = input("Apakah anda ingin mengkonversi lagi? (y/n) >> ")
            if ans4 == "y":
                main()
            elif ans4 == "n":
                print("Terima kasih telah menggunakan konversi kami.")
                time.sleep(2)
                sys.exit()
        elif ans7 == "4":
            main()

    #Exit
    elif ans == '5':
        print("\nTerima kasih telah menggunakan alat ini\n")
        time.sleep(2)
        sys.exit()

    #User Wrong Input
    elif ans != "":
        print("Maaf saya tidak mengerti maksud anda. Silahkan masukkan angka yang tersedia di menu")
        main()

main()



# Basit seviye kullanici giris uygulamasi

print("******************* ATM Giriş Paneli *******************")

kullanici_adi = "turkiye"
sifre = "iklimkrizi"

input_data_ka = input("Lütfen kullanıcı adınızı giriniz: ")
input_data_s = input("Lütfen şifrenizi giriniz: ")

if kullanici_adi != input_data_ka:
    print("Kullanıcı adınız hatalı.")
elif sifre != input_data_s:
    print("Parolanız hatalı.")
elif kullanici_adi == input_data_ka and sifre == input_data_s:
    print("Tebrikler, giriş yapıldı.")
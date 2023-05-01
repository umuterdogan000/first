

# Cümleyi aşağıdaki şekilde değiştiren fonksiyonu yazınız.

#before: "İşçi ve Emekçi Bayramımız Kutlu Olsun!"
#after: "İşÇi vE EmEkÇi bAyRaMıMıZ KuTlU OlSuN!"



def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
           new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("İşçi ve Emekçi Bayramımız Kutlu Olsun!")
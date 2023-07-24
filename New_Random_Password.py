
import random
import string

menu = """
    Seçim :
        1 ) 6'lı .
        2 ) 12'li .
        3 ) 24'lü .
        Q ) Çıkış .
"""

print(menu)
vote = input(" Lütfen seçim yapınız : ")

symbol = string.punctuation
number = string.digits
lower_Case = string.ascii_lowercase
big_Case = string.ascii_uppercase

characters = symbol + number + lower_Case + big_Case

def password_1() :
    password = random.choices(characters, k=6)
    password = ''.join(password)

    print(" New Random Password (6) : ", password)

def password_2() :
    password = random.choices(characters, k=12)
    password = ''.join(password)

    print(" New Random Password (12) : ", password)

def password_3() :
    password = random.choices(characters, k=24)
    password = ''.join(password)

    print(" New Random Password (24) : ", password)

def exit() :
    print(" Çıkış yapılıyor . ")
    quit()

def warning() :
    print(" Hatalı giriş yaptınız . \n Uygulamayı yeniden başlatınız .")
    quit()

if vote == "1" :
    password_1()

elif vote == "2" :
    password_2()

elif vote == "3" :
    password_3()

elif vote == "q" or vote == "Q" :
    exit()

else :
    warning()



# Bu oyunu yazarken random kütüphanesinden yararlanacağız.

# Random kütüphanesi ile bilgisayar bizim belirteceğimiz iki sayı arasında
# rastgele bir sayı üretecek

# Kullanıcının tahmin hakkı 7 olacak

# Kullanıcı üretilen sayıyı tahmin ederse kazanacak

# Kullanıcının tahmini üretilen sayıdan büyük ise kullanıcıya çok büyük diyecek

# Kullanıcının tahmini üretilen sayıdan küçük ise kullanıcıya çok küçük diyecek

# Geçersiz girişlerde kullanıcıya geçersiz giriş yaptığını söyleyecek sadece 1 - 100 veya belirlenen aralıkta bir giriş yapmasını söyleyecek

# Eğer 7 hakkı dolarsa ve kullanıcı sayıyı tahmin edemezse kaybedecek ve üretilen sayıyı görecek


import random # -> Rastgele sayı üretmek için

number = random.randint(1, 100) # -> 1-100 arası rastgele sayı

GUESS_COUNT = 7 # -> Kullanıcının tahmin hakkı










































"""import random

print("Hi! Welcome to the Number Guessing Game."
      "\nYou have 7 chances to guess the number. Let's Start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low}"
      f"and {high}. Let's start!")

      
num = random.randint(low, high)
ch = 7 # total allowed chances
gc = 0 # guess counter

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} attemps.")
        break
    
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")

    elif guess > num:
        print("Too high! Try a lower number.")

    elif guess < num:
        print("Too low! Try a higher number.")"""
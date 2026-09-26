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

ATTEMPT = 7 # -> Kullanıcının tahmin hakkı


print("\nSayı Bulma Oyununa Hoşgeldiniz") 
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
print(f"\nTahmin hakkınız {ATTEMPT} adet. Başarılar!")
print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")



while True:
    guess = input("1 ile 100 arasında bir sayı tahmin edin: ") # -> Kullanıcıdan tahmin alıyoruz

    
    if guess == 'q':
        print("Oyundan çıkılıyor...")
        break
    
    
    guess = int(guess)
    
    if guess != number:
        ATTEMPT -= 1 # -> Kullanıcının tahmin hakkını azaltıyoruz
        print(f"\nKalan tahmin hakkınız: {ATTEMPT}")
        
        if ATTEMPT == 0:
            print(f"\nÜzgünüm. Tuttuğum sayı: {number}. Bir dahaki sefere şansını dene!")
            break
        
    if guess < 1 or guess > 100:
        print("Geçersiz giriş! Lütfen 1 ile 100 arasında bir sayı giriniz.")

    elif guess == number:
        print(f"Tebrikler. Tuttuğum sayı: {number}")
        print(f"{7 - ATTEMPT} tahminde sayıyı buldunuz.")

    elif guess > number:
        print("Tahmininiz çok büyük. Daha küçük bir sayı deneyin.")

    elif guess < number:
        print("Tahmininiz çok küçük. Daha büyük bir sayı deneyin.")
        
    else:
        print(f"Üzgünüm. Tuttuğum sayı: {number}. Bir dahaki sefere şansını dene!")



































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
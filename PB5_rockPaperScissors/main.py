import random, sys

print('TAŞ, KAĞIT, MAKAS ')

# Bu değişkenler galibiyet, yenilgi ve beraberlik sayısını tutar.
wins = 0
losses = 0
ties = 0

while True: # Ana oyun göngüsü
    print('%s Galibiyet, %s Yenilgi, %s Beraberlik' % (wins, losses, ties))
    
    while True: # Oyuncu girdi döngüsü
        print('Hamlenizi giriniz: (t)aş, (k)ağıt, (m)akas veya (q)uit çıkış')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Programdan çık.
            
        if playerMove == 't' or playerMove =='k' or playerMove == 'm':
            break # Oyuncu girdi döngüsünden çık
        print('t, k, m ya da q giriniz...')
    
    # Oyuncunun hamlesini yazdır
    if playerMove == 't':
        print('TAŞA karşı....')
        
    elif playerMove == 'k':
        print('KAĞIDA karşı....')
        
    elif playerMove == 'm':
        print('MAKASA karşı....')
        
    # Bilgisayarın hamlesini seç
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 't'
        print('TAŞ')
        
    elif randomNumber == 2:
        computerMove = 'k'
        print('KAĞIT')
        
    elif randomNumber == 3:
        computerMove = 'm'
        print('MAKAS')
        
    
    # Galibiyet, yenilgi ve beraberlik durumlarını görüntülü ve kaydet
    if playerMove == computerMove:
        print('Berabere!')
        ties += 1
        
    elif playerMove == 't' and computerMove == 'm':
        print('TAŞ MAKASI kırar. Kazandınız!')
        wins += 1
        
    elif playerMove == 'k' and computerMove == 't':
        print('KAĞIT TAŞI sarar. Kazandınız!')
        wins += 1
        
    elif playerMove == 'm' and computerMove == 'k':
        print('MAKAS KAĞIDI keser. Kazandınız!')
        wins += 1
        
    elif playerMove == 't' and computerMove == 'k':
        print('KAĞIT TAŞI sarar. Kaybettiniz.')
        losses += 1
        
    elif playerMove == 'k' and computerMove == 'm':
        print('MAKAS KAĞIDI keser. Kaybettiniz.')
        losses += 1
        
    elif playerMove == 'm' and computerMove == 't':
        print('TAŞ MAKASI kırar. Kaybettiniz.')
        losses += 1
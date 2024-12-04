import time
from random import uniform

def mulai_game(berapa_kali=1):
    nama = input('Masukan nama karakter: ')
    MAX = 10

    while True:
        power = int(input('Masukan power karakter: '))
        sprint = int(input('Masukan sprint karakter: '))
        accuracy = int(input('Masukan accuracy karakter: '))
        total = power + sprint + accuracy
        if total > MAX:
            print(f'Total stat gak boleh lebih dari {MAX}')
        else:
            break

    for _ in range(berapa_kali):
        boss = 10
        start = time.time()
        while boss > 0:
            damage = (power * uniform(0.5, 1.5)) * (accuracy * uniform(0.5, 1.5))
            print(f'Attack boss with {damage:.2f} damage')
            boss -= damage
            if boss >= 0:
                print(f'Health boss: {boss:.2f}')
            time.sleep(1 / (sprint + 1))
        end = time.time()
        
        died = end - start
        print(f'Boss died in {died:.2f} seconds')

        with open('data.txt', 'a') as fp:
            fp.write(f'Nama: {nama} - Record: {died}\n')



def lihat_leaderboard():
    with open('data.txt', 'r') as fp:
        data = fp.read()
    
    for i, d in enumerate(data.split('\n')):
        print(f'{i + 1} - {d}')


while True:
    print('Mau ngepain?')
    print('1. Main')
    print('2. Lihat leaderboard')
    print('3. Exit')
    masukan = input('Masukan: ')
    pilihan = int(masukan)
    if pilihan == 1:
        mulai_game()
    elif pilihan == 2:
        lihat_leaderboard()
    elif pilihan == 3:
        break
    else:
        print('Pilihan tidak valid')
        


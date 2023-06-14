import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates

def format_date(x, pos=None):
    return mdates.num2date(x).strftime('%Y-%m-%d')

def get_hisse_listesi():
    hisseler = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']  # Örnek hisse listesi
    return hisseler

def hisse_secimi():
    hisse_listesi = get_hisse_listesi()
    print("Lütfen bir hisse seçin:")
    for i, hisse in enumerate(hisse_listesi):
        print(f"{i + 1}. {hisse}")
    secim = int(input("Seçiminizi yapın (1-4 arası bir sayı): "))
    return hisse_listesi[secim - 1]

def grafikleri_goster(hisse_simbolu):
    hisse_verileri = yf.download(hisse_simbolu, start="2022-01-01", end="2023-06-13")

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    son_3gun = hisse_verileri['Close'].tail(3)
    axs[0, 0].plot(son_3gun)
    axs[0, 0].set_title('Günlük Grafik (Son 3 Gün)')
    axs[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    son_9gun = hisse_verileri['Close'].tail(9)
    axs[0, 1].plot(son_9gun)
    axs[0, 1].set_title('Haftalık Grafik (Son 9 Gün)')
    axs[0, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    son_32gun = hisse_verileri['Close'].tail(32)
    axs[1, 0].plot(son_32gun)
    axs[1, 0].set_title('Aylık Grafik (Son 32 Gün)')
    axs[1, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    son_12ay = hisse_verileri['Close'].tail(12 * 22)  # 22 iş günü kabul ederek
    axs[1, 1].plot(son_12ay)
    axs[1, 1].set_title('Yıllık Grafik (Son 12 Ay)')
    axs[1, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.tight_layout()
    plt.show()

def menu_goster():
    print("1. Hisse Listesini Görüntüle")
    print("2. Hisse Seçimi Yap")
    print("3. Seçilen Hisse İçin Grafikleri Göster")
    print("0. Çıkış")
    secim = input("Seçiminizi yapın: ")
    return secim

while True:
    secim = menu_goster()

    if secim == "1":
        hisse_listesi = get_hisse_listesi()
        print("Hisse Listesi:")
        for hisse in hisse_listesi:
            print(hisse)

    elif secim == "2":
        secilen_hisse = hisse_secimi()
        print(f"Seçilen hisse: {secilen_hisse}")

    elif secim == "3":
        secilen_hisse = hisse_secimi()
        grafikleri_goster(secilen_hisse)

    elif secim == "0":
        break

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
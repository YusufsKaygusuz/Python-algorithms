import matplotlib.pyplot as plt
import numpy as np

class HisseTakipUygulamasi:
    def __init__(self):
        self.hisseler = {}
    
    def hisse_ekle(self, hisse_kodu, alis_fiyati):
        self.hisseler[hisse_kodu] = {
            'alis_fiyati': alis_fiyati,
            'son_fiyat': alis_fiyati,
            'fiyatlar': [alis_fiyati]
        }
    
    def hisse_guncelle(self, hisse_kodu, son_fiyat):
        if hisse_kodu in self.hisseler:
            self.hisseler[hisse_kodu]['son_fiyat'] = son_fiyat
            self.hisseler[hisse_kodu]['fiyatlar'].append(son_fiyat)
            self.kar_zarar_kontrol(hisse_kodu)
    
    def kar_zarar_kontrol(self, hisse_kodu):
        alis_fiyati = self.hisseler[hisse_kodu]['alis_fiyati']
        son_fiyat = self.hisseler[hisse_kodu]['son_fiyat']
        
        kar_orani = (son_fiyat - alis_fiyati) / alis_fiyati * 100
        
        if kar_orani > 5:
            print(f"{hisse_kodu} hissesinde %{kar_orani:.2f} oranında kar elde ettiniz.")
        elif kar_orani < -5:
            print(f"{hisse_kodu} hissesinde %{kar_orani:.2f} oranında zarar ettiniz.")
    
    def hisse_grafik(self, hisse_kodu):
        if hisse_kodu in self.hisseler:
            fiyatlar = self.hisseler[hisse_kodu]['fiyatlar']
            
            plt.plot(np.arange(len(fiyatlar)), fiyatlar)
            plt.xlabel('Gün')
            plt.ylabel('Fiyat')
            plt.title(f"{hisse_kodu} Hisse Fiyatları")
            plt.show()
        else:
            print(f"{hisse_kodu} hissesi bulunamadı.")
    
    def run(self):
        while True:
            print("1 - Hisse ekle")
            print("2 - Hisse güncelle")
            print("3 - Hisse grafiği")
            print("4 - Çıkış")
            
            secim = input("Bir seçenek girin (1-4): ")
            
            if secim == '1':
                hisse_kodu = input("Hisse kodunu girin: ")
                alis_fiyati = float(input("Alış fiyatını girin: "))
                self.hisse_ekle(hisse_kodu, alis_fiyati)
            elif secim == '2':
                hisse_kodu = input("Hisse kodunu girin: ")
                son_fiyat = float(input("Son fiyatı girin: "))
                self.hisse_guncelle(hisse_kodu, son_fiyat)
            elif secim == '3':
                hisse_kodu = input("Hisse kodunu girin: ")
                self.hisse_grafik(hisse_kodu)
            elif secim == '4':
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçim!")

# Uygulamanın kullanımı
uygulama = HisseTakipUygulamasi()
uygulama.run()
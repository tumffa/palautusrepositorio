from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly


class KPS:
    def __init__(self, tekoaly=None):
        self._tekoaly = tekoaly

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._anna_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._anna_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def _anna_siirto(self, ekan_siirto=None):
        return 0
    
    @staticmethod
    def luo_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def luo_pelaaja_vs_tekoaly():
        return KPSTekoaly(Tekoaly())
    
    @staticmethod
    def luo_pelaaja_vs_parannettu_tekoaly():
        return KPSTekoaly(TekoalyParannettu(10))

class KPSPelaajaVsPelaaja(KPS):
    def __init__(self):
        super().__init__()

    def _anna_siirto(self, ekan_siirto=None):
        return input("Toisen pelaajan siirto: ")
    
class KPSTekoaly(KPS):
    def __init__(self, tekoaly):
        super().__init__(tekoaly)

    def _anna_siirto(self, ekan_siirto=None):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        if ekan_siirto:
            self._tekoaly.aseta_siirto(ekan_siirto)
        return siirto

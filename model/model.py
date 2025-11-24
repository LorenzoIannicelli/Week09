from database.meteo_dao import MeteoDao

class Model:
    def __init__(self):
        self._costo_minimo = -1
        self._soluzione_ottima = []

    def get_umidita_media_mese(self, mese):
        return MeteoDao.get_umidita_media_mese(mese)

    def get_situazione_meta_mese(self, mese):
        return MeteoDao.get_umidita_media_mese(mese)

    def genera_sequenza(self, mese):
        situazione_meta_mese = self.get_situazione_meta_mese(mese)
        self._ricorsione([], situazione_meta_mese)
        return self._soluzione_ottima, self._costo_minimo

    def _ricorsione(self, parziale, situazioni):
        if len(parziale) == 15:
            print(parziale)
            costo = self._calcola_costo(parziale)
            if costo < self._costo_minimo or self._costo_minimo == -1:
                self._costo_minimo = costo
                self._soluzione_ottima = parziale
        else :
            giorno = len(parziale)+1

            for situazione in situazioni[(giorno-1)*3 : giorno*3] :
                if self.vincoli_soddisfatti(parziale, situazione):
                    parziale.append(situazione)
                    self._ricorsione(parziale, situazioni)
                    parziale.pop()

    def vincoli_soddisfatti(self, parziale, situazione) :
        counter = 0
        for fermata in parziale:
            if fermata.localita == situazione.localita:
                counter += 1
        if counter > 6 :
            return False

        if len(parziale) > 0 and len(parziale) <= 2 :
            if situazione.localita != parziale[0].localita :
                return False

        elif len(parziale) > 2 :
            sequenza_finale = parziale[-3:]
            counter = 0
            for fermata in sequenza_finale :
                if fermata.localita == situazione.localita :
                    counter += 1
            if counter < 3 and situazione.localita != sequenza_finale[-1].localita :
                return False

        return True

    def _calcola_costo(self, parziale):
        costo = 0
        ultima_fermata = parziale[0]
        for fermata in parziale :
            costo += fermata.umidita
            if fermata.localita != ultima_fermata.localita :
                costo += 100

            ultima_fermata = fermata

        return costo
from metaflow import FlowSpec, step

class kuliahinformatikaflow(FlowSpec):

    @step
    def start(self):
        """Membayar spp 1"""
        print("Membayar SPP Pertama")
        self.next(self.ambil_krs)

    @step
    def ambil_krs(self):
        """Mengambil KRS"""
        print("Mengambil KRS")
        self.next(self.dapat_jadwal)

    @step
    def dapat_jadwal(self):
        """Mendapat jadwal kuliah"""
        print("Mendapat jadwal kuliah")
        self.next(self.kuliah_1)

    @step
    def kuliah_1(self):
        """Mengikuti perkuliahan"""
        print("Mengikuti perkuliahan dan tugas 1")
        self.next(self.uts)

    @step
    def uts(self):
        """Mengikuti ujian tengah semester"""
        print("Mengikuti UTS")
        self.next(self.kuliah_2)

    @step
    def kuliah_2(self):
        """Mengikuti perkuliahan"""
        print("Mengikuti perkuliahan dan tugas 2")
        self.next(self.bayar_spp2)

    @step
    def bayar_spp2(self):
        """Membayar spp 2"""
        print("Membayar SPP Kedua")
        self.next(self.uas)

    @step
    def uas(self):
        """Mengikuti ujian akhir semester"""
        print("Mengikuti UAS")
        self.next(self.end)

    @step
    def end(self):
        """Mendapat nilai KHS"""
        print("Mendapatkan nilai KHS")

if __name__ == '__main__':
    kuliahinformatikaflow()

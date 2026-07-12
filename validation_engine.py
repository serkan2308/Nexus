class ValidationEngine:
    def __init__(self):
        print("Validation Engine: Aktif. Analiz süreci başlatılıyor...")

    def analyze_and_route(self, data):
        # The brain analyzes words
        print("Validation Engine: Veri analiz ediliyor...")
        
        # Middle Reset çağrısı yapılacak
        self.middle_reset()
        
        return "Data routed to Error Detecting Engine"

    def middle_reset(self):
        print("Validation Engine: Middle Reset uygulandı. Hafıza temizlendi.")

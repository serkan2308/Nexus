from data_box import DataBox
from validation_engine import ValidationEngine
from error_detecting import ErrorDetectingEngine
from filtering_func import FilteringFunction
from error_brain_memory import ErrorBrainMemory

class NexusCore:
    def __init__(self):
        print("Nexus Core: Sistem başlatılıyor...")
        self.box = DataBox()
        self.validator = ValidationEngine()
        self.detector = ErrorDetectingEngine()
        self.filter = FilteringFunction()
        self.memory = ErrorBrainMemory()

    def run_cycle(self, user_input):
        print(f"\n--- Yeni İşlem Döngüsü ---")
        
        # 1. Veriyi kutuya al
        self.box.store(user_input)
        
        # 2. Doğrulama ve Analiz
        self.validator.analyze_and_route(user_input)
        
        # 3. Hata Taraması
        self.detector.detect(user_input)
        
        # 4. Filtreleme
        self.filter.filter(user_input)
        
        # 5. Hafızaya Kayıt
        self.memory.store_experience(user_input)
        
        print("Nexus Core: Döngü başarıyla tamamlandı.\n")

# Nexus'u başlatma denemesi
if __name__ == "__main__":
    nexus = NexusCore()
    nexus.run_cycle("Test Verisi")

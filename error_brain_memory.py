class ErrorBrainMemory:
    def __init__(self):
        self.memory = []
        print("Error Brain Memory: Hafıza merkezi aktif. Öğrenmeye hazır.")

    def store_experience(self, data):
        # Hatalı veya temiz veriyi hafızaya alıp öğrenme süreci
        self.memory.append(data)
        print(f"Error Brain Memory: Yeni deneyim kaydedildi. Toplam kayıt: {len(self.memory)}")

    def recall(self):
        return self.memory

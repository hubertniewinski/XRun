from models.HistoryProperty import HistoryProperty


class HealthInformation:
    def __init__(self, birthDate, sex, height, weight):
        self.birthDate = birthDate
        self.sex = sex
        self.height = height
        self.weight = HistoryProperty("weight", weight)
        self.bodyFatPercentage = HistoryProperty("bodyFatPercentage", None)
        self.leanBodyMass = HistoryProperty("leanBodyMass", None)
        self.restingHeartRate = HistoryProperty("restingHeartRate", None)
        self.maximumHeartRate = HistoryProperty("maximumHeartRate", None)
        self.lactateThreshold = HistoryProperty("lactateThreshold", None)

    def __str__(self):
        return f"HealthInformation(birthDate={self.birthDate}, sex={self.sex}, height={self.height}, weight={self.weight}, bodyFatPercentage={self.bodyFatPercentage}, leanBodyMass={self.leanBodyMass}, restingHeartRate={self.restingHeartRate}, maximumHeartRate={self.maximumHeartRate}, lactateThreshold={self.lactateThreshold})"

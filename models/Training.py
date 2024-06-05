class Training:
    def __init__(self, distance, avgPace, time, date, elevation, avgHeartRate, calories):
        self.distance = distance
        self.avgPace = avgPace
        self.time = time
        self.date = date
        self.elevation = elevation
        self.avgHeartRate = avgHeartRate
        self.calories = calories

    def __str__(self):
        return f"Training(distance={self.distance}, avgPace={self.avgPace}, time={self.time}, date={self.date}, elevation={self.elevation}, avgHeartRate={self.avgHeartRate}, calories={self.calories})"

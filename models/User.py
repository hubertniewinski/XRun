from typing import List

from models.HealthInformation import HealthInformation
from models.RunningGoal import RunningGoal
from models.Training import Training


class User:
    def __init__(self, id, birthDate, sex, height, weight, runningGoal: RunningGoal, trainings: List[Training], city, country):
        self.id = id
        self.healthInformation = HealthInformation(birthDate, sex, height, weight)
        self.runningGoal = runningGoal
        self.trainings = sorted(trainings, key=lambda x: x.date)
        self.city = city
        self.country = country
    
    def __str__(self):
        formatted_trainings = [str(training) for training in self.trainings]
        return f"User(healthInformation={self.healthInformation}, \ntrainings={formatted_trainings}, \nrunningGoal={self.runningGoal})"
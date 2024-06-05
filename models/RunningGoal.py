class RunningGoal:
    def __init__(self, deadline, distance, time):
        self.deadline = deadline
        self.distance = distance
        self.time = time

    def __str__(self):
        return f"RunningGoal(deadline={self.deadline}, distance={self.distance}, time={self.time})"

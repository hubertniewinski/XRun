from rich import print as rprint

from models.Training import Training
from models.User import User
from models.RunningGoal import RunningGoal
from save.save import loadUser, saveUser


def addTraining(user: User):
    rprint("[yellow]Type informations about training...[/yellow]")
    distance = input("Distance: ")
    avg_pace = input("Average pace: ")
    time = input("Time: ")
    date = input("Date: ")
    elevation = input("Elevation: ")
    avg_heart_rate = input("Average heart rate: ")
    calories = input("Calories: ")
    training = Training(distance, avg_pace, time, date, elevation, avg_heart_rate, calories)
    user.trainings.append(training)
    saveUserDecorator(user)
    return user


def initializeUser():
    rprint("[yellow]Loading user...[/yellow]")
    user = loadUser()

    if user is None:
        rprint("[yellow]User not found. Provide some information about you[/yellow]")
        birthday = input("Birthday: ")
        gender = input("Gender: ")
        height = input("Height: ")
        weight = input("Weight: ")
        city = input("City: ")
        country = input("Country: ")

        rprint("[yellow]Thanks. Now define your running goal[/yellow]")
        deadline = input("When you want achieve goal: ")
        distance = input("Distance: ")
        time = input("Time: ")

        running_goal = RunningGoal(deadline, distance, time)
        user = User(1, birthday, gender, height, weight, running_goal, [], city, country)
        saveUserDecorator(user)
    else:
        rprint("[yellow]User loaded successfully...[/yellow]")

    return user


def saveUserDecorator(user: User):
    rprint("[yellow]All set. Saving user...[/yellow]")
    saveUser(user)
    rprint("[yellow]User saved successfully [/yellow]")

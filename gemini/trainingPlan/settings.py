from models.ModelOptions import ModelOptions
from models.User import User
from weather.weather import get_weather

__session_key = 'TODAY_TRAINING_PLAN'
__system_instruction = ("It will provide you with information about the person. Based on it, propose a training plan "
                        "for today. Please try to take into account all the information provided in the first call. "
                        "Each subsequent one will be a direct interaction with the user and you can develop a plan "
                        "based on this")


def getTrainingPlanModelOptions(user: User):
    weather = get_weather(user.city, user.country)
    weather_obj = {
        'main': weather['main'],
        'weatherDescription': weather['weather'][0]['description'],
    }
    weather_str = "weather={" + str(weather_obj) + "}"
    return ModelOptions(__session_key, __system_instruction, [], str(user) + "\n" + weather_str)

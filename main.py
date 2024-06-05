from gemini.session import start
from update.update import update
from user.initialize import initializeUser, addTraining

user = initializeUser()
print(user)

add_training_action_name = 'add_training'
edit_user_action_name = 'edit_user'
chat_action_name = 'chat'

actions = [add_training_action_name, chat_action_name, edit_user_action_name]

while True:
    for index, action in enumerate(actions):
        print(f"{index + 1}) '{action}'")

    user_input = input("Enter an action name")

    if user_input == add_training_action_name:
        user = addTraining(user)
    elif user_input == chat_action_name:
        start(user)
    elif user_input == edit_user_action_name:
        update(user)
    else:
        print("Invalid input")
import asyncio
import os

from rich import print as rprint

from gemini.globalSettings import models
from gemini.trainingPlan.settings import getTrainingPlanModelOptions
from models import ModelOptions
from models.User import User


def beginChatSession(modelOptions: ModelOptions):
    """
    Install the Google AI Python SDK

    $ pip install google-generativeai

    See the getting started guide for more information:
    https://ai.google.dev/gemini-api/docs/get-started/python
    """
    import google.generativeai as genai

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel(
        model_name=modelOptions.model_name,
        safety_settings=modelOptions.safety_settings,
        generation_config=modelOptions.generation_config,
        system_instruction=modelOptions.system_instruction,
    )
    chat_session = model.start_chat(history=modelOptions.history)
    return chat_session


def start(user: User):
    models.append(getTrainingPlanModelOptions(user))

    print(
        "Welcome to XRrun assistant. Im here to help you achieve your goals. Type category from listed below or type "
        "'quit' to quit.")

    valid_keys = [model_option.session_key for model_option in models]

    while True:
        for index, model_option in enumerate(models):
            print(f"{index + 1}) '{model_option.session_key}'")

        user_input = input("Enter a session key or 'quit' to exit: ")

        if user_input.lower() == 'quit':
            break
        elif user_input in valid_keys:
            print(f"You selected {user_input}")
            model = next((model for model in models if model.session_key == user_input), None)
            asyncio.run(startSession(model))
            break
        else:
            print("Invalid input. Please try again.")


async def startSession(modelOptions: ModelOptions):
    current_session = beginChatSession(modelOptions)
    first_call = True
    while True:
        rprint(f"[yellow]Chat category: {modelOptions.session_key}[/yellow]")

        user_input = ''
        if first_call and modelOptions.firstCallMessage is not None:
            first_call = False
            user_input = modelOptions.firstCallMessage
        else:
            user_input = input(f"Type something or 'quit' to quit: ")

        if user_input == 'quit':
            break

        print(f"User input: {user_input}")
        rprint("[yellow]Loading...[/yellow]")

        response = await current_session.send_message_async(user_input)

        rprint(f"[green]RESPONSE:[/green] [blue]{response.text}[/blue]")

        user_input_history = {
            "role": "user",
            "parts": [user_input]
        }
        model_output_history = {
            "role": "model",
            "parts": [
                response.text
            ]
        }
        current_session.history.append(user_input_history)
        current_session.history.append(model_output_history)
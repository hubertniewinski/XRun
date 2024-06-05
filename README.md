# 🏃‍♂️ XRun: A Personalized Training App Powered by AI and Weather Data

XRun is a Python console application designed to provide personalized training plans and injury advice, leveraging the power of the Gemini API and OpenWeather API. The application utilizes user information and current weather conditions to create a tailored experience.

## Key Features:

- **User Information Tracking and Management:** XRun allows users to create and edit their personal information, including health data and training history. Specific properties like weight are instances of the `HistoryProperty` class, which maintains a record of values, enabling progress tracking over time.
- **AI-Powered Training and Health Support:** XRun offers a range of AI-powered features through its integration with the Gemini API. This includes:
    - **Daily Training Plan Generation:** The application generates a customized training plan for the current day, taking into account the user's individual information.
    - **Injury Advice:** XRun provides personalized advice based on the user's reported injuries.
    - **Customizable Topics:** Users can easily add new custom topics and messages to the Gemini API by creating a `ModelOptions` class and adding it to the `globalSettings.py` file.
- **Weather Integration:** XRun enhances the training plan by incorporating real-time weather data. The application determines the user's location and retrieves current weather conditions from the OpenWeather API. This information is then passed to the Gemini API for generating the most relevant Daily Training Plan.

## Prerequisites:

- **VPN:** A VPN is required if the user's location is not valid for the Gemini API.
- **Environment Variables:** The following environment variables must be set:
    - `GEMINI_API_KEY`: Your Gemini API key.
    - `WEATHER_API_KEY`: Your OpenWeather API key.

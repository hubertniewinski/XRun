class ModelOptions:
    model_name = "gemini-1.5-flash-latest"

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    def __init__(self, session_key, system_instruction, history = [], firstCallMessage = None, modelName=model_name, safetySettings=safety_settings,
                 generationConfig=generation_config):
        self.session_key = session_key
        self.system_instruction = system_instruction
        self.history = history
        self.firstCallMessage = firstCallMessage
        self.model_name = modelName
        self.safety_settings = safetySettings
        self.generation_config = generationConfig

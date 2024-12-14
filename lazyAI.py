import google.generativeai as genai
genai.configure(api_key="")
class ChatSession:
    def __init__(self):

        generation_config = {
        "temperature": 0.1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 2000,
        "response_mime_type": "text/markdown",
        }
        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
        ]
        self.model = genai.GenerativeModel(model_name='gemini-1.5-flash', safety_settings=safety_settings, system_instruction="Turn this thought into a well written paragraph" )
        self.chat = self.model.start_chat(history=[])

    def send_message(self, message):
        if message == "Let's start":
            response = "Let's get started!"
        else:
            response = self.chat.send_message(message)
            response.resolve()
            response.text
        return response

    def get_chat_history(self):
        return self.chat.history

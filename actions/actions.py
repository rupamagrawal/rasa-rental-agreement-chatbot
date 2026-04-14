# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

class ActionExplainClause(Action):

    def name(self):
        return "action_explain_clause"

    def run(self, dispatcher, tracker, domain):

        user_input = tracker.latest_message.get("text")

        prompt = f"""
        You are a legal assistant.

        Explain the rent agreement clause in SIMPLE terms.

        Also classify risk level as: LOW, MEDIUM, or HIGH.

        Format:

        Explanation:
        - (2-3 short points)

        Risks:
        - (2-3 short points)

        Risk Level:
        - (LOW / MEDIUM / HIGH with 1 line reason)

        Keep answer under 80 words.

        Clause:
        {user_input}
        """

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"        
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        result = response.json()

        if len(user_input.split()) < 4:
            dispatcher.utter_message(text="Please provide a full clause to analyze.")
            return []
        
        try:
            if "candidates" in result:
                output = result["candidates"][0]["content"]["parts"][0]["text"]
            elif "error" in result:
                output = "API Error: " + result["error"]["message"]
            else:
                output = str(result)
        except Exception as e:
            output = f"Error processing response: {str(e)}"
        # disclaimer
        dispatcher.utter_message("⚠️ Not legal advice\n")
        dispatcher.utter_message(output)

        return []
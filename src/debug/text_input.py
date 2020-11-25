from ..agent import agent;
import dialogflow
from google.api_core.exceptions import InvalidArgument

def debug_text_input():

    while True:
        text_to_be_analyzed = input("Input: ")

        text_input = dialogflow.types.TextInput(
            text=text_to_be_analyzed, 
            language_code=agent.language_code
        )
        query_input = dialogflow.types.QueryInput(text=text_input)

        try:
            response = agent.session_client.detect_intent(
                session=agent.session, query_input=query_input)
        except InvalidArgument:
            raise

        print("Detected intent:", response.query_result.intent.display_name)
        print("Detected intent confidence:",
            response.query_result.intent_detection_confidence)
        print("Fulfillment text:", response.query_result.fulfillment_text)
        print("Quit: ctrl + c")
        print("------------------------")
import dialogflow_v2
from google.api_core.exceptions import InvalidArgument

class _Agent:
    language_code = "en-US"
    def __init__(self): 
        self.session_client = dialogflow_v2.SessionsClient()
        self.session = self.session_client.session_path(
            project="gamingspeechcontroller-uttr", 
            session="should_this_be_random_for_every_run" # TODO What should be here
        )

# Create an global agent
agent = _Agent()
import dialogflow_v2 as dialogflow

from .speech_gui import SpeechGUI
from .agent import agent;
from .microphone import microphone
from .intents import Intents

def detectIntentFromSpeech(microphoneStream, speechGUI: SpeechGUI):
    audioEncoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = microphone.RATE

    def requestGenerator(audioConfig):
        queryInput = dialogflow.types.QueryInput(audio_config=audioConfig)

        # The first request contains the configuration.
        yield dialogflow.types.StreamingDetectIntentRequest(
            session=agent.session, query_input=queryInput)

        while True:
            chunk = microphoneStream.read(microphone.CHUNK)
            if not chunk:
                break
            # The later requests contains audio data.
            yield dialogflow.types.StreamingDetectIntentRequest(
                input_audio=chunk)

    audioConfig = dialogflow.types.InputAudioConfig(
        audio_encoding=audioEncoding,
        single_utterance=True,
        language_code=agent.language_code,
        sample_rate_hertz=sample_rate_hertz,
    )

    requests = requestGenerator(audioConfig)
    responses = agent.session_client.streaming_detect_intent(requests)

    print('=' * 20)
    lastResponse = None
    for response in responses:
        lastResponse = response
        transcript = response.recognition_result.transcript

        print('Intermediate transcript: "{}".'.format(transcript))
        speechGUI.changeText(transcript)
        shortcutIntent = _findShortcutIntent(transcript)
        if shortcutIntent:
            return shortcutIntent, None

    # Note: The result from the last response is the final transcript along
    # with the detected content.
    queryResult = lastResponse.query_result

    print('=' * 20)
    print('Query text: {}'.format(queryResult.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        queryResult.intent.display_name,
        queryResult.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        queryResult.fulfillment_text))

    return queryResult.intent.display_name, queryResult.parameters


def _findShortcutIntent(transcript):
    """
        Only short and commands that do not overlap with other 
        more longer commands should be added here. If no shortcut
        intent is found, None is returned
    """
    
    goShortcut = ["ok", "okay", "continue"];
    if transcript in goShortcut:
        return Intents.GO

    return None;
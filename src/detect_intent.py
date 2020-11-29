import dialogflow_v2 as dialogflow
from .agent import agent;
from .microphone import microphone

def detectIntentFromSpeech(microphoneStream):
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
        print('Intermediate transcript: "{}".'.format(
                response.recognition_result.transcript))

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
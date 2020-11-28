import dialogflow_v2 as dialogflow
from .agent import agent;
from .microphone import microphone

def detect_intent_from_speech(microphone_stream):
    audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = microphone.RATE

    def request_generator(audio_config):
        query_input = dialogflow.types.QueryInput(audio_config=audio_config)

        # The first request contains the configuration.
        yield dialogflow.types.StreamingDetectIntentRequest(
            session=agent.session, query_input=query_input)

        while True:
            chunk = microphone_stream.read(microphone.CHUNK)
            if not chunk:
                break
            # The later requests contains audio data.
            yield dialogflow.types.StreamingDetectIntentRequest(
                input_audio=chunk)

    audio_config = dialogflow.types.InputAudioConfig(
        audio_encoding=audio_encoding,
        single_utterance=True,
        language_code=agent.language_code,
        sample_rate_hertz=sample_rate_hertz,
    )

    requests = request_generator(audio_config)
    responses = agent.session_client.streaming_detect_intent(requests)

    print('=' * 20)
    last_response = None
    for response in responses:
        last_response = response
        print('Intermediate transcript: "{}".'.format(
                response.recognition_result.transcript))

    # Note: The result from the last response is the final transcript along
    # with the detected content.
    query_result = last_response.query_result

    print('=' * 20)
    print('Query text: {}'.format(query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        query_result.intent.display_name,
        query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        query_result.fulfillment_text))

    return query_result.intent.display_name, query_result.parameters
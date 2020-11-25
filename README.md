# GamingSpeechController

## Development setup

### Add credentials for Dialogflow
* Ask Adam for the gaming_speech_controller_service_account.json file
  * Put it somewhere (I do not need to be in the project folder)
    * Tip: Create a folder in the project root named "private" and put the file there. This folder is ignored by git
* Follow the instruction beginning at "Use the service account key file in your environment" at the following site: https://cloud.google.com/dialogflow/es/docs/quick/setup
  * You do not need to create your own service account.
  * The path for the "GOOGLE_APPLICATION_CREDENTIALS" variable should be pointing at the file Adam gave.
  * May not be required: "Install and initialize the Cloud SDK"
  * May not be required: "Test the SDK and authentication"
  * **DO NOT** skip "Install the Dialogflow client library"
* Done

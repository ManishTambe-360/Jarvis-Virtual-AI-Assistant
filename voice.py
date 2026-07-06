from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv(dotenv_path="E:/JARVIS/.env")

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",  # "Adam" - browse voices at elevenlabs.io/app/voice-library
    model_id="eleven_multilingual_v2"
)

play(audio)


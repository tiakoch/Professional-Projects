import fitz
from google.cloud import texttospeech
import os


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    doc.close()
    return text


def text_to_speech(text, output_audio_path="output.mp3"):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_audio_path, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio saved as {output_audio_path}")


def main():
    pdf_path = input("Enter the path to the PDF file: ")

    if not os.path.exists(pdf_path):
        print("Error: File not found. Please check the path and try again.")
        return

    text = extract_text_from_pdf(pdf_path)

    if text.strip():
        output_audio_path = os.path.splitext(pdf_path)[0] + ".mp3"
        text_to_speech(text, output_audio_path)
    else:
        print("No text found in the PDF.")


if __name__ == "__main__":
    main()





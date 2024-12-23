pip install SpeechRecognition
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

st.title("Audio to Text Converter")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Display audio player
    st.audio(uploaded_file, format='audio/wav')

    # Process audio
    try:
        # Create a temporary file path for the uploaded audio
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Initialize recognizer
        r = sr.Recognizer()

        # Load audio file
        with sr.AudioFile("temp_audio.wav") as source:
            audio_data = r.record(source)

        # Recognize speech
        text = r.recognize_google(audio_data)
        
        st.success("Transcription successful!")
        st.write("Transcribed Text:")
        st.write(text)

    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

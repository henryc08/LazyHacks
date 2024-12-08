import lazyAI
import os
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, flash
from lazyAI import ChatSession
# from speechtotext import main
import asyncio
import threading
from threading import Thread
import speechtotext
import shared_state
import math
import random
import time
import keyboard
import speech_recognition as sr
import pyautogui

# lazyAI.ChatSession.send_message(speechtotext.text)

chat_session = None
response = ""
app = Flask(__name__)
app.secret_key = os.urandom(24)
messages = ""
chat_sessions = [ChatSession()]
gemini_responses = 0

import speech_recognition as sr
from lazyAI import ChatSession # shariq stuff
import time
import os
import threading
import shared_state
import asyncio
import keyboard
# from websockets.asyncio.client import connect
# Initialize the recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()  # Ensure we initialize microphone only once
recording = False
recorded_text = ""  # Store the recorded audio data

# Initialize the recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()  # Ensure we initialize microphone only once
recording = False
recorded_text = ""  # Store the recorded audio data


def callback(recognizer, audio):
    """
    Background callback function to process audio.
    This is called whenever audio is captured by listen_in_background.
    """
    global recording, recorded_text

    try:
        # Attempt to recognize speech with a timeout
        detected_text = recognizer.recognize_google(audio).lower()
        print(f"[Callback] Detected Speech: {detected_text}")

        if not recording and "i'm feeling lazy" in detected_text:
            # If the start phrase is detected, begin recording
            recording = True
            recorded_text = ""  # Clear the recorded text
            print("[Callback] Start phrase detected. Recording has begun.")
            keyboard.write("Let's start")
            keyboard.press_and_release("Enter")


        elif recording and "i'm tired" in detected_text:
            # If the stop phrase is detected, stop recording
            recording = False
            print("[Callback] Stop phrase detected. Stopping recording.")
            print(f"[Callback] Recorded text: {recorded_text}")
            pyautogui.hotkey('command', 'a')
            keyboard.press_and_release('delete')
            keyboard.write(recorded_text)
            keyboard.press_and_release("Enter")
            time.sleep(1)  # Sleep to prevent immediate restart
            print("[Main] Listening in the background for phrases...")

        elif recording:
            recorded_text += detected_text + ". "
            print(f"[Callback] Updated text: {recorded_text}")
            keyboard.write(recorded_text)
            
    except sr.UnknownValueError:
        print("[Callback] Speech not understood, retrying...")
    except sr.RequestError as e:
        print(f"[Callback] API request error: {e}")
    except Exception as e:
        print(f"[Callback] Unexpected exception: {e}")


def main2():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise levels
        print("[Main] Ambient noise adjusted.")

    print("[Main] Listening in the background for phrases...")
    # Set up background recording with better logging
    stop_recording = recognizer.listen_in_background(microphone, callback)

    try:
        # Main loop with controlled sleep to prevent CPU hogging
        while True:
            time.sleep(0.1)  # Controlled loop sleep
    except KeyboardInterrupt:
        print("\n[Main] KeyboardInterrupt detected. Stopping background listener...")
    except Exception as e:
        print(f"[Main] Unexpected exception: {e}")
    finally:
        # Stop the listener and clean up properly
        stop_recording()
        print("[Main] Listener stopped.")
        print(f"[Main] Final recorded text: {recorded_text}")  


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/switch_session', methods=["POST"])
def switch_session():
    print("hello")

    return jsonify({'message': "test successful"})

    # for msg in chat_session.get_chat_history():
    #     a = str(msg.parts[0])
    #     if msg.role == "user":
    #         print(a[7:len(a)-2])
    #         # receive_message(a[7:len(a)-2])
    #         return jsonify({'message': a[7:len(a)-2]})
    #     elif msg.role == "model":
    #         print(a[7:len(a)-2])
    #         # send_message(a[7:len(a)-2])
    #         return jsonify({'message': a[7:len(a)-2]})
    #     print(chat_session.get_chat_history())
    
    # print(chat_session.get_chat_history())
    # return jsonify({'message': str(chat_session.get_chat_history())})

@app.route('/send_message', methods=['POST'])
def send_message(answer = None):
    global response
    global messages
    global gemini_responses
    if not answer == None:
        return jsonify({'message': answer})
    else:
        message = request.json.get('message')
        messages = message + messages
        gemini_responses += 1
        response = chat_sessions[0].send_message(message)
        print(chat_sessions[0].get_chat_history())
        return jsonify({'message': response.text})

@app.route('/receive_message')
def receive_message(answer = None):
    global response
    global gemini_responses
    if response == "Let's get started!":
        return jsonify({'message': response})
    if gemini_responses == 7:
        return jsonify({'message': response})
    else:
        return jsonify({'message': response.text})


if __name__ == '__main__':
    main_thread = threading.Thread(target=main2) 
    main_thread2 = threading.Thread(target=app.run) 
    main_thread.start()
    main_thread2.start()
    

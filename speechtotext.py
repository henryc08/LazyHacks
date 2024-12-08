import speech_recognition as sr
import time


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

        elif recording and "i'm tired" in detected_text:
            # If the stop phrase is detected, stop recording
            recording = False
            print("[Callback] Stop phrase detected. Stopping recording.")
            print(f"[Callback] Recorded text: {recorded_text}")
            time.sleep(1)  # Sleep to prevent immediate restart
            print("[Main] Listening in the background for phrases...")

        elif recording:
            recorded_text += detected_text + ". "
            print(f"[Callback] Updated text: {recorded_text}")

    except sr.UnknownValueError:
        print("[Callback] Speech not understood, retrying...")
    except sr.RequestError as e:
        print(f"[Callback] API request error: {e}")
    except Exception as e:
        print(f"[Callback] Unexpected exception: {e}")


def main():
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


if __name__ == "__main__":
    main()

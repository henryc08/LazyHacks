# TALK 2 ME 🎙️🖊️🔥 

Way to LAZY to get up and type? Well, you're in luck, because **Talk 2 Me (T2M)** is your AI-powered writing assistant designed to make typing obsolete! Simply speak your thoughts, and T2M transforms them into beautiful writing that can be used in professional and educational situations!!!

Whether you’re brainstorming, completing assignments, or just jotting down ideas, T2M makes it effortless. Chat with your AI, switch between conversations, and refine your writing—all through an intuitive interface. 

**IMPORTANT: To begin recording, simply say "I'm feeling lazy", to end the recording, say "I'm tired".**

---

## Inspiration 🌟

We’re all tired of typing everything out all the time, so we asked ourselves: why type when you can talk? Imagine completing homework assignments straight from your bed—no laptop, just your voice.

To make this dream a reality, we leveraged AI to create a "lazy" but highly effective solution.

---

## What It Does 🛠️

**Talk 2 Me (T2M)** is an AI-powered tool designed to take informal and unorganized speech and transform it into beautifully written, sophisticated paragraphs. Here’s how it works:

1. **Automated Speech-to-Text 🎙️➡️📜:** T2M listens in the background for "I'm feeling lazy" to begin recording, then uses Python's speech recognition library to convert your voice into a text prompt. The end phrase is "I'm tired". 
2. **AI Processing 🤖:** The text is sent to the Gemini AI API, which generates polished responses.
3. **Chat Interface 💬:** The responses are displayed in a chat-styled UI. Each chat session is stored, enabling you to switch between different conversations seamlessly.
4. **Keyboard Integration ⌨️:** You can also input text manually, prompting the AI to critique and refine paragraphs further.

---

## Features ✨

- **Voice-to-Text Conversion:** Quickly translate your spoken words into text.
- **AI-Powered Refinement:** Get sophisticated and polished paragraphs.
- **Chat Session Management:** Easily switch between saved conversations.
- **Keyboard Input:** Refine or critique content through manual prompts.

---

## Challenges We Faced 🚧

1. **Language Interoperability 🌐:** Running the speech-to-text program in Python while hosting the website required a bridge between Python and HTML. We had to learn and implement JavaScript and WebSockets as intermediaries, which was entirely new to us.
2. **Speech Accuracy 🎯:** Ensuring accurate speech recognition and managing start and stop prompts was tricky.

---

## Accomplishments We’re Proud Of 🏆

- **User Interface 🎨:** Developing a clean, minimalistic, and intuitive UI.
- **Speech-to-Text 🎤:** Successfully integrating functional voice-to-text capabilities.
- **AI Integration 🤝:** Seamlessly connecting the AI to the UI for a smooth user experience.
- **End-to-End Workflow 🔄:** Seeing everything come together as a functional product.

---

## Next Steps 🚀

1. **Voice Response 🔊:** Enable the program to read out AI-generated responses.
2. **End Prompt Detection 🤔:** Remove the need for a manual end prompt by allowing the AI to detect when the user’s speech ends.

---

## Built With 🛠️

- **Python 🐍:** For speech recognition and backend logic.
- **HTML & CSS/SCSS 🌐:** For structuring and styling the web interface.
- **JavaScript 💻:** To enable communication between the frontend and backend via WebSockets.

---

## How to Use 📖

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/henryc08/T2M---LazyHacks.git
   cd T2M---LazyHacks

2. **Install Dependencies**: Ensure you have [Python] installed.

  - Install Python dependencies:
     ```bash
     pip install -r requirements.txt

  - Install Node.js dependencies:
    ```bash
    npm install
   
3. **Run the backend server**:
   ```bash
   python main.py

4. **Serve the Frontend**:

Open the local server in your web browser to view the interface.

5. **Start Talking**:

Use your microphone to speak and watch your thoughts transform into polished paragraphs in real-time.
**IMPORTANT: To begin recording, simply say "I'm feeling lazy", to end the recording, say "I'm tired".**

---

## Contributing
Contributions, bug reports, and suggestions are welcome!
Feel free to fork the repo and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Credits
- Developed by Henry Cai, Shariq Charolia, Timothy Riddolls, and Ryan Zhao
- Thanks to the creators of the SpeechRecognition library and Gemini AI API for making this project possible.
- Shoutout to LazyHacks for an amazing hackathon!

---

DoraHacks: [https://dorahacks.io/buidl/20535/]



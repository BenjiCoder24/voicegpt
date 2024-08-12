# Voice GPT Interface

## Overview

This project is a Flask-based web application designed to process WAV audio files and extract basic information about them, returning a text-based transcript of the audio content. The application is built to be simple and robust, providing a friendly interface for recording and processing audio data.

## Features

- **Audio Recording**: Users can record audio directly through their browser using the provided interface.
- **Audio Processing**: The server processes the uploaded WAV files to extract data such as channel count, rate, sample width, and duration.
- **Transcription Simulation**: The server simulates a transcription process, returning a placeholder text as the "transcription" of the uploaded audio.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **JavaScript**: For handling client-side scripting including audio recording and server communication.
- **HTML/CSS**: For structuring and styling the web interface.

## Setup and Running the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository.git
   cd your-project-directory
   ```
2. **Install Dependencies**
   ```bash
   pip install Flask flask-cors wave
   ```
3. **Environment Variables**

   - Ensure you have a `.env` file containing the necessary environment variables such as `OPENAI_API_KEY`.

4. **Run the Application**

   ```bash
   python app.py
   ```

   This will start the Flask server on `localhost` with the default port `5000`.

5. **Access the Application**
   Open a web browser and go to `http://localhost:5000` to use the application.

## Usage

- Click the **Record** button to start recording your voice.
- Click again to stop recording and automatically upload the recording for processing.
- View the processed data as it appears below the recording button.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome to improve the application, add new features, or fix bugs.

## License

This project is open-source and available under the MIT License.

# Chatbot Knowledge Embedding Project

## Description

This project implements a Python-based chatbot that leverages knowledge embedding from a CSV file. The chatbot can answer questions based on data embedded using a machine learning model.

## Project Structure

- `chatbot.py`  
  Main script to run the chatbot and handle user interaction.

- `knowledge_embed.py`  
  Script for embedding knowledge from the CSV file into a format usable by the chatbot.

- `data_knowledge.csv`  
  Knowledge data file containing information for the chatbot.

- `ca.pem`  
  CA certificate for secure connections (if required).

- `.env/`  
  Python virtual environment for managing project dependencies.

## Installation

1. **Activate the virtual environment**  
   Run the following command in your terminal:
   ```sh
   source .env/Scripts/activate
   ```

2. **Install dependencies**  
   Make sure all dependencies are installed in the virtual environment. If not, install them with:
   ```sh
   pip install -r requirements.txt
   ```
   *(Ensure you have a `requirements.txt` file listing your dependencies)*

## Usage

1. **Embed Knowledge**  
   Run the embedding script:
   ```sh
   python knowledge_embed.py
   ```

2. **Run the Chatbot**  
   Start the chatbot:
   ```sh
   python chatbot.py
   ```

## Configuration

- Ensure the `.env` folder is properly set up as your Python environment.
- The `ca.pem` file is used for secure connections to external services if needed.

## License

This project is licensed as you require.

---

**Contributors:**  
- Your Name

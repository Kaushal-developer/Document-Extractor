import gradio as gr
import sqlite3
import os
import json
from markitdown import MarkItDown
from openai import OpenAI
import re
from dotenv import load_dotenv
load_dotenv()

# Initialize MarkItDown with OpenAI
client = OpenAI(api_key=os.environ.get('OPEN_API_KEY'))
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

# Create SQLite database
DB_FILE = "documents.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            filepath TEXT,
            classification TEXT,
            json_data TEXT
        )
    """)
    conn.commit()
    conn.close()


# Function to classify & extract JSON
def process_document(file):
    try:
        # Process with MarkItDown
        result = md.convert(file)
        original_text = result.text_content

        # OpenAI Chat Completion for JSON extraction
        response = client.chat.completions.create(
            model="gpt-3.5",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Analyze the provided document text and extract structured information in JSON format. "
                        "Identify key fields such as 'document_type', 'personal_details' (name, date of birth, gender, contact details), "
                        "'document_details' (document number, issuance/expiration dates, issuing authority). "
                        "Ensure the output JSON is structured properly and contains relevant data."
                    )
                },
                {
                    "role": "user",
                    "content": original_text
                }
            ]
        )

        # Extract and clean JSON from OpenAI response
        classification = response.choices[0].message.content.strip()
        cleaned_json = re.sub(r'```json\n|\n```', '', classification)  # Remove markdown JSON formatting

        try:
            doc_info = json.loads(cleaned_json)  # Convert JSON string to dictionary
        except json.JSONDecodeError:
            doc_info = {"error": "Invalid JSON extracted from OpenAI response."}  # Handle JSON errors

        # Store result in SQLite
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO documents (filename, filepath, classification, json_data) VALUES (?, ?, ?, ?)",
            (file.split('/')[-1], file, classification, json.dumps(doc_info))  # Convert dictionary to JSON string
        )
        conn.commit()
        conn.close()

        return classification, doc_info
    except Exception as e:
        return "Error", {"error": str(e)}


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📄 Document Classification & JSON Extraction")
    file_input = gr.File(label="Upload PDF or JPG")
    classify_button = gr.Button("Classify Document")
    classification_output = gr.Textbox(label="Classification", interactive=False)
    json_output = gr.JSON(label="Extracted JSON Data")

    classify_button.click(fn=process_document, inputs=[file_input], outputs=[classification_output, json_output])

# Run Gradio App
if __name__ == "__main__":
    demo.launch()

# 📌 Document Extractor POC

🚀 **Extract and process text from documents using Microsoft's MarkItDown**

## 📖 Overview
The **Document Extractor POC** is a proof of concept (POC) application designed to extract text from documents (PDFs, images, etc.) using Microsoft's open-source **MarkItDown** package. This project demonstrates how **AI-powered text extraction** can be used to process and structure document content efficiently.

---

## 🎯 Key Features
✅ Text extraction from images & PDFs  
✅ AI-driven content structuring using **MarkItDown**  
✅ Support for multiple document formats  
✅ Easy integration into existing applications  

---

## ⚙️ Prerequisites
Before setting up the project, ensure you have the following installed:

- **Python (≥ 3.9)**
- **pip** (latest version)
- **Virtual Environment** (optional but recommended)
- **Git**

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
# Clone the repository
git clone https://github.com/Kaushal-developer/document-extractor-poc.git
cd document-extractor-poc
```

### 2️⃣ Create & Activate Virtual Environment (Optional but Recommended)

#### For **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

#### For **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install MarkItDown Package
Since **MarkItDown** is an open-source package from Microsoft, install it directly from GitHub:
```bash
pip install git+https://github.com/microsoft/markitdown.git
```

---

## 🚀 Usage
### Basic Example
You can use **MarkItDown** in Python to convert documents into structured text:

```python
from markitdown import MarkItDown
from openai import OpenAI

# Initialize OpenAI client (if applicable)
client = OpenAI()

# Initialize MarkItDown with AI model
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

# Convert an image or PDF to structured text
result = md.convert("example_document.jpg")

# Print extracted content
print(result.text_content)
```

---

## 📂 Project Structure
```bash
📦 document-extractor-poc
┣ 📂 data            # Sample input files (PDFs, images)
┣ 📂 output          # Extracted text outputs
┣ 📜 requirements.txt # Required dependencies
┣ 📜 main.py         # Main script for document processing
┣ 📜 README.md       # Project documentation
┣ 📜 .gitignore      # Git ignore file
```

---

## 🛠 Troubleshooting

### 1️⃣ MarkItDown Installation Issues
- Ensure you have **Python 3.9+** installed.
- If `pip install` fails, upgrade pip:
  ```bash
  pip install --upgrade pip
  ```
- If installation from GitHub fails, clone the repo manually:
  ```bash
  git clone https://github.com/microsoft/markitdown.git
  cd markitdown
  pip install .
  ```

### 2️⃣ File Processing Issues
- Ensure the file format is **supported** (`.jpg`, `.png`, `.pdf`).
- Check if **OpenAI API key** is set correctly (if using AI processing).

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 💡 Future Enhancements
✅ Add support for **batch processing** of documents  
✅ Implement **web UI** for document uploads  
✅ Enhance **error handling & logging**  

---

## 🤝 Contributing
We welcome contributions! To contribute:
1. **Fork** the repo.
2. **Create** a new branch (`feature-x`).
3. **Submit** a Pull Request.

---

## 📩 Contact
👨‍💻 **Kaushal J Kanani**  
✉️ Email: [kaushal.developer@yahoo.com](mailto:kaushal.developer@yahoo.com)  
🔗 LinkedIn: [Kaushal Kanani](https://www.linkedin.com/in/kaushal-kanani-896aa6138/)  

---

**🚀 Happy Coding!**


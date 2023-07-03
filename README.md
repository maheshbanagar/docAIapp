 
# docAIapp

A streamlit application where we can upload a document as png/pdf, run OCR using tesseract

## Implementation

- Create a virtual environment 

- Install necessary libraries
```bash
  pip install streamlit Image pytesseract pdf2image
```
- Download the tesseract using this [link](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe)

- set tesseract path (change this to the path on your system)
```bash
  pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'
```
- Run the application
```bash
 streamlit run <fileName.py>
```

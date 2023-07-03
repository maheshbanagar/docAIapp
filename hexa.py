import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
from pdf2image import convert_from_bytes

# Set Tesseract path (change this to the path on your system)
pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'

def ocr(image):
    # Perform OCR using Tesseract
    result = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    return result

def draw_boxes(image, result):
    boxes = result['text']
    for i in range(len(boxes)):
        if int(result['conf'][i]) > 60:  # Adjust confidence threshold as per your needs
            (x, y, w, h) = (result['left'][i], result['top'][i], result['width'][i], result['height'][i])
            image = image.copy()
            draw = ImageDraw.Draw(image)
            draw.rectangle([(x, y), (x + w, y + h)], outline='red', width=2)
    
    return image

def main():
    st.title("Document OCR with bounding boxes")
    uploaded_file = st.file_uploader("Upload a document (PNG or PDF)", type=["png", "pdf"])
    
    if uploaded_file is not None:
        try:
            # Convert uploaded file to image
            if uploaded_file.type == 'application/pdf':
                images = convert_from_bytes(uploaded_file.read())
                image = images[0]  # Select the first page of the PDF
            else:
                image = Image.open(uploaded_file)
            
            st.image(image, caption="Uploaded Document", use_column_width=True)
            
            # Perform OCR and draw bounding boxes
            result = ocr(image)
            image_with_boxes = draw_boxes(image, result)
            st.image(image_with_boxes, caption="OCR Result with Bounding Boxes", use_column_width=True)
            
            # Display extracted text
            st.header("Extracted Text")
            for text in result['text']:
                st.write(text+" ")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.warning("Please make sure the uploaded file is in PNG or PDF format.")
    
if __name__ == "__main__":
    main()

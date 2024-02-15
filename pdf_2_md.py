import os
from PyPDF2 import PdfReader

def convert_pdf_to_md(input_dir='input', output_dir='output'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith(".pdf"):
            # Define the PDF and MD file paths
            pdf_path = os.path.join(input_dir, pdf_file)
            md_file = os.path.splitext(pdf_file)[0] + ".md"
            md_path = os.path.join(output_dir, md_file)

            # Read the PDF file using PdfReader
            with open(pdf_path, 'rb') as file:
                reader = PdfReader(file)
                num_pages = len(reader.pages)

                # Extract text and write to MD file
                with open(md_path, 'w') as md_file:
                    for page_num in range(num_pages):
                        page = reader.pages[page_num]
                        text = page.extract_text()
                        md_file.write(text if text else '')
                        md_file.write('\n\n') # Add space between pages

if __name__ == "__main__":
    convert_pdf_to_md()

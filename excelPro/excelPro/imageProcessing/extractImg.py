import fitz  # PyMuPDF
import os
from pdftoimg import read_text_from_images_in_folder

dir = ''

def extract_images_from_pdf(pdf_path, output_folder):
    global dir  # Declare that we are using the global variable

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Update the global dir variable with the path of the exported images
    dir = output_folder

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # List to store image file paths
    image_files = []

    # Loop through each page of the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        image_list = page.get_images(full=True)

        # Loop through the images
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = os.path.join(output_folder, f"page_{page_number+1}_image_{img_index+1}.png")

            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)

            image_files.append(image_filename)

            print(f"Extracted image saved to: {image_filename}")

    pdf_document.close()

    # Create export folder in the same directory as the script
    export_folder = os.path.join(output_folder, 'exported_images')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    for i, image_file in enumerate(image_files):
        new_image_filename = os.path.join(export_folder, f"image_{i+1}.png")
        os.rename(image_file, new_image_filename)
        print(f"Image moved to: {new_image_filename}")

    # Update the global dir variable with the path of the exported images
    dir = export_folder

# Example usage
extract_images_from_pdf('/home/dinesh/Documents/Spring/demo/excelPro/excelPro/testing/ok2.pdf', '/home/dinesh/Documents/Spring/demo/excelPro/imageProcessing/')
print(f"Global dir path: {dir}")

# Ensure images are properly moved before reading
read_text_from_images_in_folder(dir)

import easyocr
import re
import os
from spellchecker import SpellChecker

def correct_spelling(text):
    spell = SpellChecker()
    corrected_text = spell.correction(text)
    return corrected_text

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def contextual_correction(text):
    corrections = {
        "recieve": "receive",
        "teh": "the",
    }
    words = text.split()
    corrected_words = [corrections.get(word, word) for word in words]
    return ' '.join(corrected_words)

def post_process_text(text):
    text = normalize_text(text)
    text = correct_spelling(text)
    text = contextual_correction(text)
    return text

import os
import easyocr
import re
from spellchecker import SpellChecker

# Define global variables and functions for text processing
def correct_spelling(text):
    spell = SpellChecker()
    corrected_text = spell.correction(text)
    return corrected_text

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def contextual_correction(text):
    corrections = {
        "recieve": "receive",
        "teh": "the",
    }
    words = text.split()
    corrected_words = [corrections.get(word, word) for word in words]
    return ' '.join(corrected_words)

def post_process_text(text):
    text = normalize_text(text)
    text = correct_spelling(text)
    text = contextual_correction(text)
    return text

# Function to read text from a single image
def read_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path)

    print(f"Detecting words in {image_path} and combining them.")
    
    # Combine and post-process the results
    full_text = ' '.join([result[1] for result in results])
    processed_text = post_process_text(full_text)
    
    return processed_text

# Function to read text from all images in a folder
def read_text_from_images_in_folder(folder_path):
    all_texts = []
    
    # Loop through each image in the folder
    for filename in sorted(os.listdir(folder_path)):
        if filename.startswith("image_") and (filename.endswith(".png") or filename.endswith(".jpg")):
            image_path = os.path.join(folder_path, filename)
            image_text = read_text_from_image(image_path)
            all_texts.append(image_text)
            
            # Delete the image after processing
            os.remove(image_path)
    
    # Combine all the extracted texts into a single paragraph
    combined_text = ' '.join(all_texts)
    
    # Print the combined text as a paragraph
    print(f"Detected text: '{combined_text}'")

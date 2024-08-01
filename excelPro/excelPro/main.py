import re
import pandas as pd
from io import StringIO
from pdfminer.high_level import extract_text
from gemini_module import create_model, send_message


# Create the model
model = create_model()

# Extract text from the PDF file
pdf_path = '/home/dinesh/Documents/Spring/demo/excelPro/excelPro/Resume.pdf'
text = extract_text(pdf_path)

# Example text with special characters
text_with_special_chars = text

# Define a regular expression pattern to match non-ASCII characters
pattern = re.compile(r'[^\x20-\x7E]')

# Replace all non-ASCII characters with a hyphen

### Note: The output of text_replaced contain double hyphen '->>' before and after in some words

text_replaced = pattern.sub('->', text_with_special_chars)
response = send_message(model, text_replaced )

# Input string
input_string = response

# Use StringIO to treat the string as a file-like object
data = StringIO(input_string)

# Read the string into a DataFrame
df = pd.read_csv(data)

# Write the DataFrame to a CSV file
df.to_csv("output.csv", index=False)
print("String written to output.csv")

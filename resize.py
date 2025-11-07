import os
from PIL import Image

# Configuration
input_folder = "input_images"
output_folder = "output_images"
new_width = 800
new_height = 600
convert_format = "JPEG"

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process images
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        with Image.open(file_path) as img:
            resized_img = img.resize((new_width, new_height))
            name, ext = os.path.splitext(filename)
            output_file = os.path.join(output_folder, f"{name}.{convert_format.lower()}")
            resized_img.save(output_file, convert_format)
            print(f"Resized and saved: {output_file}")

print("All images resized successfully!")

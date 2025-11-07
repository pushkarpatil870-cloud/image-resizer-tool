# Image Resizer

A simple Python script to **batch resize and convert images** in a folder. This tool is ideal for automating image processing tasks such as resizing photos for websites, social media, or storage optimization.

## Features
- Resize multiple images in a folder at once.
- Convert images to a different format (JPEG, PNG, etc.).
- Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`.
- Automatically creates an output folder for resized images.
- Easy to customize width, height, and output format.

## Requirements
- Python 3.x
- Pillow library

Install Pillow via pip:

```bash
pip install Pillow
Usage
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/Image-Resizer.git
Place images to resize in the input_images folder.

Open resize.py and configure your desired width, height, and format.

Run the script:

bash
Copy code
python resize.py
Check the output_images folder for resized images.

Folder Structure
css
Copy code
Image-Resizer/
├─ input_images/      ← Place original images here
├─ output_images/     ← Resized images will be saved here
└─ resize.py          ← Python script to resize images
# PDF Merging Script

## Overview

The PDF Merging Script is a simple Python utility that allows you to merge multiple PDF files into a single PDF document. This script utilizes the PyPDF2 library to perform the merging operation.

## Requirements

- Python 3.x
- PyPDF2 library

## Usage

1. Make sure you have Python 3.x installed on your system.

2. Install the PyPDF2 library if you haven't already by running the following command:
   ```bash
   pip3 install PyPDF2
   ```

3. Place your PDF files that you want to merge in the same directory as the script or provide the full path to the files.

4. Run the script from the command line, providing the input PDF file names you want to merge and the output PDF file name as arguments (last file name will be the output file name):
   ```bash
   python3 pdf-merger.py input1.pdf input2.pdf input3.pdf output.pdf
   ```

   - Replace `input1.pdf`, `input2.pdf`, and `input3.pdf` with the PDF files you want to merge.
   - Replace `output.pdf` with the desired name of the merged PDF.

5. The script will merge the specified input PDF files into a single output PDF file.

## Note

- Ensure that the input PDF files exist in the specified locations.
- The output file will be created in the same directory where the script is located.

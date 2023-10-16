#!/usr/bin/env python3

import PyPDF2
import argparse
import sys

def merge_pdfs(pdf_files, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()
    
    # Adding each pdf to merger
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)
    
    # Creating the output file
    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)
    
    pdf_merger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge multiple PDF files into one.')
    parser.add_argument('input_pdfs', nargs='+', help='PDF files to merge')
    parser.add_argument('output_pdf', help='Output PDF file')
    
    args = parser.parse_args()
    
    try:
        merge_pdfs(args.input_pdfs, args.output_pdf)
        print(f"PDF's Merged Successfully into {args.output_pdf}")
    except PyPDF2.utils.PdfReadError:
        print("Error: One or more input files are not valid PDFs.")
    except FileNotFoundError:
        print("Error: One or more input files do not exist.")

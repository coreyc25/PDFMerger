import PyPDF2
import sys

def merge_pdfs(paths, output):
    pdf_merger = PyPDF2.PdfMerger()
    for path in paths:
        pdf_merger.append(path)
    with open(output, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python merge_pdfs.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        sys.exit(1)

    output_pdf_path = sys.argv[1]
    input_pdf_paths = sys.argv[2:]
    
    merge_pdfs(input_pdf_paths, output_pdf_path)
    print(f'Merged PDFs into {output_pdf_path}')

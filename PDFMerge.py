import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    with open(pdf1_path, 'rb') as pdf1, open(pdf2_path, 'rb') as pdf2:
        pdf_merger.append(pdf1)
        pdf_merger.append(pdf2)
        pdf_merger.write(output_path)

if __name__ == "__main__":
    pdf1_path = r"first.pdf" #first file path
    pdf2_path = r"second.pdf" #second file path
    output_path = r"output.pdf" #output file path
    
    merge_pdfs(pdf1_path, pdf2_path, output_path) #function call
    print("PDF files merged successfully!")
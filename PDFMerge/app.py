from flask import Flask, render_template, request, send_file
import PyPDF2
import os

app = Flask(__name__)

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    pdf_merger.append(pdf1_path)
    pdf_merger.append(pdf2_path)
    pdf_merger.write(output_path)
    pdf_merger.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf1 = request.files["pdf1"]
        pdf2 = request.files["pdf2"]

        if pdf1 and pdf2:
            pdf1_path = os.path.join("uploads", pdf1.filename)
            pdf2_path = os.path.join("uploads", pdf2.filename)
            pdf1.save(pdf1_path)
            pdf2.save(pdf2_path)

            output_path = os.path.join("uploads", "merged_output.pdf")
            merge_pdfs(pdf1_path, pdf2_path, output_path)

            return send_file(output_path, as_attachment=True)
    
    return render_template("index.html")

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.mkdir("uploads")
    app.run(debug=True)

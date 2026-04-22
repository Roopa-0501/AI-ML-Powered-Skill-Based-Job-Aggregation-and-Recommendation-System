from PyPDF2 import PdfReader

def pdf_to_text(file):
    reader = PdfReader(file)
    text = ""


    for page in reader.pages:
        text += page.extract_text() or ""

    return text.lower()



# from PyPDF2 import PdfReader
# import docx

# def pdf_to_text(file):

#     filename = file.filename.lower()

#     try:
#         # 🔹 PDF
#         if filename.endswith(".pdf"):
#             reader = PdfReader(file)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#             return text.lower()

#         # 🔹 TXT
#         elif filename.endswith(".txt"):
#             return file.read().decode("utf-8").lower()

#         # 🔹 DOCX
#         elif filename.endswith(".docx"):
#             doc = docx.Document(file)
#             text = "\n".join([p.text for p in doc.paragraphs])
#             return text.lower()

#         # 🔹 IMAGE (skip for now)
#         elif filename.endswith((".jpg", ".jpeg", ".png")):
#             return ""   # or later OCR

#         else:
#             return ""

#     except Exception as e:
#         print("File parsing error:", e)
#         return ""

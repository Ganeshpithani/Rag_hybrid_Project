# from langchain_docling.loader import DoclingLoader
from langchain_community.document_loaders import PyPDFLoader
import os
loader=PyPDFLoader(r"E:\Rag_hybrid1\2507.19595v3.pdf")
#weblink
# FILE_PATH = "https://arxiv.org/pdf/2507.19595"
# loader = DoclingLoader(file_path=FILE_PATH)
# documents = loader.load()
# # print(len(documents))
# print(os.listdir())
# # #pdfloader
# loader=DoclingLoader(file_path=r"2507.19595v3.pdf")
# documents=loader.load()
# print(len(documents))



from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


loader=PyPDFLoader(r"E:\Rag_hybrid1\2507.19595v3.pdf")
lc_obj=loader.load()
# print(lc_obj[0].page_content)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)
texts=text_splitter.split_documents(lc_obj)
# print(len(texts))
# print(texts[0].page_content)
# print(len(texts[0].page_content))

texts=[doc.page_content.replace("\n", " ") for doc in texts]

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",encode_kwargs={"normalize_embeddings": True})
doc_embeddings=embeddings.embed_documents(texts)

print(len(doc_embeddings))
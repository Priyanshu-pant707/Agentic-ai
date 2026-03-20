from langchain_community.document_loaders import TextLoader


data= TextLoader("notes.txt")

docs=data.load()

print(docs[0]) # pagecontent with meta deta

print(docs[0].page_content) # only page content
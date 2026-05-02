from langchain_community.document_loaders import PyPDFLoader


data = PyPDFLoader("your  pdf  location")


docs =data.load()


print(docs[0]) # pagecontent with meta deta
print(docs[0].page_content) # only page content    


# to access the page number of the pdf you have to just do docs[0].metadata["page"] and it will give you the page number of the pdf.
# docs[n] n denotes the page number
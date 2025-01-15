import os
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
import config

def setup_qa_chain(vector_store):
    #os.environ["HUGGINGFACEHUB_API_TOKEN"] = config.HUGGINGFACEHUB_API_TOKEN

    llm = HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Context: {context}\n\n"
            "Question: {question}\n\n"
        )
    )

    retriever = vector_store.as_retriever()
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": prompt_template}
    )

    return qa_chain

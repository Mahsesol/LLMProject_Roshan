from transformers import pipeline
#from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline

MODEL_NAME = "google/flan-t5-small"

hf_pipeline = pipeline(
    "text-generation",
    model=MODEL_NAME,
    max_length=256,
    do_sample=False,
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# qa/services/llm.py
from transformers import pipeline as hf_pipeline_factory
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate

#MODEL_NAME = "google/flan-t5-small"
MODEL_PATH = "/app/models/flan-t5-small"

_llm = None


def get_llm():
    global _llm
    if _llm is None:
        hf_pipe = hf_pipeline_factory(
            "text2text-generation",  # flan-t5 is seq2seq, not text-generation
            # model=MODEL_NAME,
            model=MODEL_PATH,
            max_length=256,
            do_sample=False,
        )
        _llm = HuggingFacePipeline(pipeline=hf_pipe)
    return _llm

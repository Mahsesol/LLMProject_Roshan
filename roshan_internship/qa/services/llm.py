from transformers import pipeline


class LocalLLM:
    def __init__(self):
        model_name = "sshleifer/tiny-gpt2"
        self.pipe = pipeline("text-generation", model=model_name)

    def generate(self, prompt):
        result = self.pipe(prompt, max_length=200)
        return result[0]["generated_text"]

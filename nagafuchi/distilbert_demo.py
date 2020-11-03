from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "cl-tohoku/bert-base-japanese-whole-word-masking")
distil_model = AutoModel.from_pretrained("../DistilBERT-base-jp")

print(distil_model)

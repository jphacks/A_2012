from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
model = AutoModel.from_pretrained("../DistilBERT-base-jp")
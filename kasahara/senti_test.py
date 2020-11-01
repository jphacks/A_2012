import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TFAutoModel, AdapterType

model = AutoModelForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
# model = TFAutoModel.from_pretrained(
#     "D:/Documents/A_2012/DistilBERT-base-jp", from_pt=True)

tokenizer = AutoTokenizer.from_pretrained(
    "cl-tohoku/bert-base-japanese-whole-word-masking")
adapter_path = "../sst-2"
model.load_adapter(adapter_path)


def predict(sentence):
    token_ids = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(sentence))
    input_tensor = torch.tensor([token_ids])
    outputs = model(input_tensor, adapter_names=['sst-2'])
    result = torch.argmax(outputs[0]).item()

    return 'positive' if result == 1 else 'negative'


# assert predict("すばらしいですね") == "positive"
# assert predict("全然面白くない") == "negative"
print(predict('すばらしいですね'))
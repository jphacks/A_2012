from transformers import AutoModel, AutoTokenizer
from transformers import TFAutoModel
import tensorflowjs as tfjs
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
# model = AutoModel.from_pretrained("D:/Documents/A_2012/DistilBERT-base-jp")
# model = TFAutoModel.from_pretrained("D:/Documents/A_2012/DistilBERT-base-jp", from_pt=True)
# model = TFAutoModel.from_pretrained("D:\Documents\A_2012\SentimentAnalysys", from_pt=True)
# model = TFAutoModel.from_config("D:\Documents\A_2012\SentimentAnalysys")

model.save_pretrained('tfjs-test2')

# tfjs.converters.save_keras_model(model, 'tfjs-model')
# print(tokenizer.tokenize('ワイモバとUQ月4000円の新プランで国の要請に対応 アップル歴40年初めてのApple Watch体験 ほか『今週のASCII.jp注目ニュース ベスト5 』'))

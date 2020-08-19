import numpy as np
import my_funx

from spell_correctin import SpellCorrect as correct
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf

# tf.config.experimental.set_visible_devices([], 'GPU')

def predict(sentence,model):
    
    sentence = correct([sentence])
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(sentence)
    sequences1 = tokenizer.texts_to_sequences(sentence)
    padded1 = pad_sequences(sequences1, maxlen=188, padding='post')
    p = my_funx.predict( my_funx.results(model.predict(padded1)) , my_funx.dixchk(sentence) )
    return str(np.squeeze(p))
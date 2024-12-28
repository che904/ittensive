import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Attention
from tensorflow.keras.models import Model
from transformers import TFAutoModel, AutoTokenizer

# Общие параметры
EMBEDDING_DIM = 128
LSTM_UNITS = 256
VOCAB_SIZE = 20000
MAX_LEN = 100

# 1. Базовые функции для эмбеддингов
def create_embedding_layer():
    return Embedding(input_dim=VOCAB_SIZE, output_dim=EMBEDDING_DIM, input_length=MAX_LEN)

# 2. Модель LSTM с Attention
def build_lstm_attention_model():
    input_seq = Input(shape=(MAX_LEN,))
    embedding = create_embedding_layer()(input_seq)
    lstm_output, state_h, state_c = LSTM(LSTM_UNITS, return_sequences=True, return_state=True)(embedding)
    context_vector, attention_weights = Attention()([state_h, lstm_output])
    output = Dense(VOCAB_SIZE, activation="softmax")(context_vector)
    
    model = Model(inputs=input_seq, outputs=output)
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

# 3. Загрузка предобученных моделей (BERT/GPT)
def load_transformer_model(model_name="bert-base-uncased"):
    transformer = TFAutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return transformer, tokenizer

# 4. Основная логика
if __name__ == "__main__":
    # Пример: LSTM Attention
    lstm_model = build_lstm_attention_model()
    print(lstm_model.summary())

    # Пример: BERT/GPT
    transformer_model, transformer_tokenizer = load_transformer_model("gpt2")
    
    # Тестовая запуска на BERT/GPT
    test_input = "Hello, how are you?"
    tokens = transformer_tokenizer(test_input, return_tensors="tf")
    transformer_output = transformer_model(tokens.input_ids)
    print("Transformer output shape:", transformer_output.last_hidden_state.shape)

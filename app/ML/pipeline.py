# Description: Pipeline running a model on user input.
# ML/pipeline.py

import numpy as np
import pandas as pd
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel

class Pipeline:
    """Pipeline running a model on user input."""

    def __init__(self) -> None:
        """Initializes the pipeline."""

        # Configuration for the model
        self.__config = {
            "max_seq_length": 512,
            "bert_model_name": "bert-base-uncased",
            "model_type": "bert_text",
        }

        # Initialize the BERT tokenizer
        self.__bert_tokenizer = BertTokenizer.from_pretrained(
            self.__config["bert_model_name"]
        )

        # Initialize the model
        self.__model = self.__init_model()

    def run(self, input_data: list[str]) -> float:
        """Runs the pipeline on the given input data.

        Args:
            input_data: A list of strings.

        Returns:
            A float representing the predicted value.
        """

        # Preprocess the input data
        input = self.__preprocessing(input_data)

        # Make a prediction using the preprocessed data
        result = self.__make_prediction(input)

        return result

    def __preprocessing(self, data: list[str]) -> np.ndarray:
        """Preprocesses the input data. Returns a numpy array of the preprocessed data."""

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame({"text": data})

        # Convert the 'text' column to a numpy array
        input = np.array(df["text"])

        # Tokenize the input using the BERT tokenizer
        input_ids = self.__bert_tokenizer(
            list(input), padding=True, truncation=True, return_tensors="tf", max_length=self.__config["max_seq_length"]
        )["input_ids"]

        # Pad the tokenized input to match the max sequence length
        padded_ids = tf.pad(
            input_ids, [[0, 0], [0, self.__config["max_seq_length"] - input_ids.shape[1]]]
        )

        return padded_ids

    def __make_prediction(self, input: np.ndarray) -> float:
        """Makes a prediction using the model. Returns the prediction."""

        # Make a prediction using the model
        prediction = self.__model.predict(input)[0][0]

        # Round the prediction to the nearest available value
        result = self.__round_prediction(prediction)

        return result

    def __init_model(self) -> tf.keras.models.Model:
        """Initializes the model and loads the weights."""

        # Load the BERT model
        self.__bert_model = TFBertModel.from_pretrained(self.__config["bert_model_name"])

        # Create a custom regression head for the model
        regression_head = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(1, activation="linear"),
        ])

        # Combine BERT and Regression Head
        input_ids = tf.keras.layers.Input(
            shape=(self.__config["max_seq_length"],), dtype=tf.int32
        )

        bert_output = self.__bert_model(input_ids)[0]  # BERT's output

        pooler_output = bert_output[:, 0, :]  # Pooler output

        regression_output = regression_head(pooler_output)  # Custom regression head

        model = tf.keras.models.Model(inputs=input_ids, outputs=regression_output)

        # Set BERT layers as non-trainable
        for layer in self.__bert_model.layers:
            layer.trainable = False

        # Load the weights
        model.load_weights("./app/ML/models/training_" + self.__config["model_type"] + "/cp.ckpt")

        return model

    def __round_prediction(self, value: float) -> float:
        """Rounds a given value to the nearest IELTS score."""

        available_values = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
        closest_value = min(available_values, key=lambda x: abs(x - value))
        return closest_value
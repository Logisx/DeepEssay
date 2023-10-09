# Description: A validator for IELTS essays.
# app/text_validation.py

import re

class Validator:
    """
    A validator for IELTS essays.
    """

    def __init__(self) -> None:
        self.warnings = []

    def run(self, input_data: str) -> list[str]:
        """
        Runs the validator on the given input data.

        Args:
            input_data: The input data to validate.

        Returns:
            A list of warnings, if any.
        """

        # Reset the warnings.
        self.warnings = []

        # Check the input data.
        self._check_input_data(input_data)

        # Check the input text.
        self._check_text(input_data)

        return self.warnings

    def _check_input_data(self, input_data: str) -> None:
        """
        Checks the input data and raises an exception if it is invalid.

        Args:
            input_data: The input data to check.
        """
        try:
            if input_data is None:
                self.warnings.append("The input data is None.")

            if not isinstance(input_data, str):
                self.warnings.append("The input data is not a string.")
        except:
            self.warnings.append("The input data is invalid.")

    def _check_text(self, text: str) -> None:
        """
        Checks the input text and adds warnings to the `warnings` list if any problems are found.

        Args:
            text: The input text to check.
        """

        # Check the length of the text.
        if len(text) < 80:
            self.warnings.append("The text is too short for an essay.")

        # Check the number of sentences.
        sentences = re.split(r'[.!?]', text)
        if len(sentences) < 5:
            self.warnings.append("The text does not contain enough sentences.")

        # Check the number of words.
        words = re.split(r'\W+', text)
        if len(words) < 80:
            self.warnings.append("The text does not contain enough words.")

        # Check the number of unique words.
        unique_words = set(words)
        if len(unique_words) < 50:
            self.warnings.append("The text does not contain enough unique words.")

        # Check the number of stop words.
        stop_words = []
        stop_words_count = len([word for word in words if word in stop_words])
        if stop_words_count > 0.2 * len(words):
            self.warnings.append("The text contains too many stop words.")

    @property
    def get_warnings(self) -> list[str]:
        """
        Returns the list of warnings.

        Returns:
            A list of warnings.
        """

        return self.warnings


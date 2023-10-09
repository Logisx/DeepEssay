# Description: Main file for the Flask app.
# app/main.py

import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from flask import Flask, render_template, request
from ML.pipeline import Pipeline
from app.text_validation import Validator


app = Flask(__name__)

pipeline = Pipeline()
validator = Validator()


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Index page that allows users to submit text and receive a prediction.
    """

    if request.method == "POST":
        # Get the essay text from the request form.
        essay_text: str = request.form["input_data"]

        # Check the input text for warnings.
        warnings = validator.run(essay_text)
        if warnings:
            return render_template("warning.html", warnings=warnings)

        # Run the pipeline on the essay text and get the essay grade.
        essay_grade: str = pipeline.run([essay_text])

        # Render the index template with the essay grade and submitted text.
        return render_template(
            "index.html", result=essay_grade, submitted_data=essay_text
        )
    else:
        # Render the index template with an empty essay grade and submitted text.
        return render_template("index.html", result="", submitted_data=None)


if __name__ == "__main__":
    with app.run(debug=True):
        print("Running the app...")

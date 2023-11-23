![Logo](https://github.com/Logisx/IELTS-Grading/blob/main/assets/deepessay-high-resolution-color-logo.png?raw=true)

# :page_facing_up: Table of Contents 

- [:page\_facing\_up: Table of Contents](#page_facing_up-table-of-contents)
- [:rocket: Grade your IELTS essay with BERT](#rocket-grade-your-ielts-essay-with-bert)
  - [:star: Features](#star-features)
  - [:bar\_chart: Model choice](#bar_chart-model-choice)
  - [:toolbox: Tech Stack](#toolbox-tech-stack)
  - [:file\_folder: Project structure](#file_folder-project-structure)
  - [:computer: Run Locally](#computer-run-locally)
- [:world\_map: Roadmap](#world_map-roadmap)
- [⚖️ License](#️-license)
- [🔗 Links](#-links)
# :rocket: Grade your IELTS essay with BERT

Welcome to the [IELTS Essay Grading Web Application](https://ielts-grading.azurewebsites.net/)! This web app is designed to provide users with a convenient and efficient way to have their IELTS essays assessed and receive a predicted score using a Machine Learning model.

![Version](https://img.shields.io/badge/Version-1.0-blue.svg)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) \
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.14-orange)
![BERT](https://img.shields.io/badge/BERT-NLP-ff6600)
![Docker](https://img.shields.io/badge/Docker-24.0-blue)
![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-Cloud-0089D6)
![REST](https://img.shields.io/badge/REST-API-5b68d6)


![Demo](https://github.com/Logisx/IELTS-Grading/blob/main/assets/Demo.gif?raw=true)


## :star: Features
- **Submit Essays**: Users can submit their IELTS essays directly through the web application. The process is user-friendly and straightforward.

- **Machine Learning Essay Grading**: The heart of this application is a finely-tuned BERT (Bidirectional Encoder Representations from Transformers) model. This model analyzes and assesses the submitted essays, considering a variety of linguistic and structural aspects.

- **Predicted Score**: After processing the essay, the application provides users with a predicted IELTS score. This score is an estimate of how the essay might be rated in the actual IELTS exam, helping users gauge their writing proficiency.

- **Warning functionality**: The application includes a warning feature that checks the submitted text. It will display a warning if the essay is too short or if the text does not meet the minimum requirements. This ensures that users are provided with guidance on submitting valid essays.
<img src="https://github.com/Logisx/IELTS-Grading/blob/main/assets/Warnings_demo.gif?raw=true" width="400" alt="Warnings demo">

## :bar_chart: Model choice
**Detailed training overview with EDA and Feature engineering** can be found in the [notebook](https://github.com/Logisx/IELTS-Grading/blob/main/IELTS_Grading_with_BERT.ipynb).\
**Dataset**: [IELTS Writing Scored Essays Dataset
](https://www.kaggle.com/datasets/mazlumi/ielts-writing-scored-essays-dataset)

After analysing different approaches I decided to continue with 3 models:
1. **BERT fine-tuned for a regression task**
2. **BERT output concatenated with numerical features**
3. **BERT output concatenated with numerical and binary features**
  
The model structures and corresponding Mean Absolute Error (MAE) metrics are shown in the figures below:
![Models structure](https://github.com/Logisx/IELTS-Grading/blob/main/assets/Model_structure_white.png?raw=true)
<img src="https://github.com/Logisx/IELTS-Grading/blob/main/assets/models_mae.png?raw=true" width="400" alt="Models MAE"> 

Although more complex models produce better results, after testing, it was decided to use a text model for lower latency.


## :toolbox: Tech Stack

- **Framework**: Flask
- **NLP**: TensorFlow, BERT, Hugging Face Transformers, Sklearn
- **Deployment**: Docker, Microsoft Azure
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git, GitHub
- **Testing**: REST client

## :file_folder: Project structure
```
+---app
|   |   main.py
|   |   text_validation.py
|   |   __init__.py
|   |
|   +---ML
|   |   |   pipeline.py
|   |   |   __init__.py
|   |   |
|   |   \---models
|   |       +---training_bert_num
|   |       |
|   |       +---training_bert_num_bin
|   |       |
|   |       \---training_bert_text
|   |   
|   +---static
|   |
|   \---templates
|         index.html
|         warning.html
|   
+---assets
|
|   .gitignore
|   Dockerfile
|   IELTS_Grading_with_BERT.ipynb
|   LICENSE
|   README.md
\   requirements.txt
```

## :computer: Run Locally

1. Clone the project

```bash
  git clone https://github.com/Logisx/IELTS-Grading.git
```

2. Go to the project directory

```bash
  cd my-project
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```

4. Train a model in a notebook and save the weights to:
```bash
  ./app/ML/models/training_bert_text
```
5. Start the server

```bash
  python app/main.py
```

# :world_map: Roadmap

1. **Testing features**: Develop unit tests and integrations test.
2. **Data collection**: Aggregate more data to improve accuracy.
3. **Educational insights feature**: Along with the score, the application will offer insights and suggestions for improvement, making it a valuable educational tool for those looking to enhance their writing skills.


# ⚖️ License

[MIT](https://github.com/Logisx/DeepEssay/blob/main/LICENSE)


# 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aleksandrshishkov)


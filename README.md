![Logo](https://github.com/Logisx/IELTS-Grading/blob/main/assets/deepessay-high-resolution-color-logo.png?raw=true)


# Grade your IELTS essay with BERT

Welcome to the IELTS Essay Grading Web Application! This web app is designed to provide users with a convenient and efficient way to have their IELTS essays assessed and receive a predicted score using a Machine Learning model.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 
![Demo](https://github.com/Logisx/IELTS-Grading/blob/main/assets/Demo.gif?raw=true)

## Model choice
**Detailed training overview with EDA and Feature engineering** can be found in the [notebook](https://github.com/Logisx/IELTS-Grading/blob/main/IELTS_Grading_with_BERT.ipynb).\
**Dataset**: [IELTS Writing Scored Essays Dataset
](https://www.kaggle.com/datasets/mazlumi/ielts-writing-scored-essays-dataset)

After analysing different approaches I decided to continue with 3 models:
1. **BERT fine-tuned for a regression task**
2. **BERT output concatenated with numerical features**
3. **BERT output concatenated with numerical and binary features**
  
The model structures and corresponding Mean Absolute Error (MAE) metrics are shown in the figures below:

![Models structure](https://github.com/Logisx/IELTS-Grading/blob/main/assets/Model_structure_white.png?raw=true)

![Models MAE](https://github.com/Logisx/IELTS-Grading/blob/main/assets/models_mae.png?raw=true)\
Although more complex models produce better results, after testing, it was decided to use a text model for lower latency.


## Tech Stack

- **Framework**: Flask
- **NLP**: TensorFlow, BERT, Hugging Face Transformers, Sklearn
- **Deployment**: Docker, Microsoft Azure
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git, GitHub
- **Testing**: REST client

## Features
- **Submit Essays**: Users can submit their IELTS essays directly through the web application. The process is user-friendly and straightforward.

- **Machine Learning Essay Grading**: The heart of this application is a finely-tuned BERT (Bidirectional Encoder Representations from Transformers) model. This model analyzes and assesses the submitted essays, considering a variety of linguistic and structural aspects.

- **Predicted Score**: After processing the essay, the application provides users with a predicted IELTS score. This score is an estimate of how the essay might be rated in the actual IELTS exam, helping users gauge their writing proficiency.

- **Warning functionality**: The application includes a warning feature that checks the submitted text. It will display a warning if the essay is too short or if the text does not meet the minimum requirements. This ensures that users are provided with guidance on submitting valid essays.\
<img src="https://example.com/path/to/small-image.gif" width="200" height="150" alt="Warnings demo">
## Run Locally

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

4. Start the server

```bash
  python app/main.py
```


## Roadmap

- Additional browser support

- Add more integrations


## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


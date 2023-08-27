
# Customer Churn Prediction

Welcome to the Customer Churn Prediction repository, which is a Customer Churn Prediction Flask app repository! This app is designed to predict customer churn a trained model with **90% accuracy**.

## Table of Contents

- [Customer Churn Prediction](#customer-churn-prediction)
  - [Table of Contents](#table-of-contents)
  - [Images](#images)
  - [Installation and Dependencies](#installation-and-dependencies)
  - [Working Directory](#working-directory)
  - [Working with the code](#working-with-the-code)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Images

Inputing Features :
![image](https://github.com/Rajarshi12321/Housing_predict_recommend/assets/94736350/2a1f9fff-bf1e-4533-9090-58db6502445d)

Predicted and recommended Output :
![image](https://github.com/Rajarshi12321/Housing_predict_recommend/assets/94736350/60bed2a5-52cc-4c9f-acad-421acf0db3b2)



## Installation and Dependencies

These are some required packages for our program which are mentioned in the Requirements.txt file

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- catboost
- pickle
- xgboost
- Flask
- dill
- requests
- beautifulsoup4
- bs4
- jinja2
- joblib
- librosa
- lxml





## Working Directory

```
📦Customer Churn Prediction
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┗ 📜signup.css
 ┃ ┗ 📂img
 ┃ ┃ ┣ 📜beautiful_house.jpg
 ┃ ┃ ┣ 📜default_pic.png
 ┃ ┃ ┣ 📜house_home_building_property_icon.ico
 ┃ ┃ ┗ 📜No Suitable house image found.png
 ┣ 📂templates
 ┃ ┣ 📜get_elements.py
 ┃ ┣ 📜home.html
 ┃ ┗ 📜index.html
 ┣ 📂__pycache__
 ┃ ┗ 📜utils.cpython-39.pyc
 ┣ 📜.gitignore
 ┣ 📜app.py
 ┣ 📜churn-prediction.ipynb
 ┣ 📜Cleaned_Data.csv
 ┣ 📜customer_churn_large_dataset.xlsx
 ┣ 📜LICENSE
 ┣ 📜model.pkl
 ┣ 📜preprocessing_pipeline.pkl
 ┣ 📜README.md
 ┗ 📜requirements.txt
  ```


## Working with the code


I have commented most of the neccesary information in the respective files.

To run this project locally, please follow these steps:-

1. Clone the repository:

   ```shell
   https://github.com/Rajarshi12321/Customer-Churn
   ```


2. Activating the env
  
    ```shell
    conda activate <your-env-name> 
    ```

3. Install the required dependencies by running:
   ```shell
    pip install -r requirements.txt.
    ``` 
   Ensure you have Python installed on your system (Python 3.9 or higher is recommended).<br />
   Once the dependencies are installed, you're ready to use the project.



4. Run the Flask app: Execute the following code in your terminal.
   ```shell  
    python app.py 
    ```
   

6. Access the app: Open your web browser and navigate to http://127.0.0.1:5000/ to use the House Price Prediction and Property Recommendation app.


## Usage
1. **Customer Churn Prediction:** On the app's homepage, users can input the specific features for predicting customer churn. After submitting the details, the app will process the information and display the predicted result.<br />
The accuracy of the prediction model is **90%**


## Contributing
I welcome contributions to improve the functionality and performance of the app. If you'd like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes and ensure that the code is well-documented.

3. Test your changes thoroughly to maintain app reliability.

4. Create a pull request, detailing the purpose and changes made in your contribution.



## License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

I hope this README provides you with the necessary information to get started with the Housing Price Prediction and Recommending project. 


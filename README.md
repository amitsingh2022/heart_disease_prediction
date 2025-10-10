#  Heart Disease Prediction App 🫀  

An interactive web app built with **Streamlit** and **Machine Learning** that predicts the likelihood of heart disease based on medical parameters such as age, cholesterol, blood pressure, and more.  

🔗 **Live App:** [Heart Disease Prediction App](https://heartdiseasepredictionap.streamlit.app/)  
📂 **Repository:** [GitHub Repo](https://github.com/amitsingh2022/heart_disease_prediction)

---

## 🧠 Project Overview  

Heart disease remains one of the most critical global health concerns. This app uses a **Machine Learning model (Random Forest Classifier)** to predict whether a person is likely to have heart disease based on their medical profile.  

Users can input health data such as:  
- Age  
- Gender  
- Chest Pain Type  
- Blood Pressure  
- Cholesterol Levels  
- Fasting Blood Sugar  
- Exercise-induced Angina  
- ST Depression & Slope  

The app provides a **real-time prediction** and displays a clear message indicating the level of risk.

---

## 🚀 Tech Stack  

- **Python 3.10+**  
- **Pandas, NumPy, Scikit-learn**  
- **Streamlit** for UI  
- **Matplotlib / Seaborn** for analysis (EDA)  
- **Joblib** for model serialization  

---

## ⚙️ How It Works  

1. The dataset is preprocessed (missing values, encoding, scaling).  
2. Features are selected and fed into a **Random Forest Classifier**.  
3. The trained model is saved using `joblib`.  
4. The Streamlit app loads the model and predicts based on user input.  

---

## 📊 Model Performance  

- **Accuracy:** ~86%  
- **Precision & Recall:** Tuned for medical context (focus on minimizing false negatives).  
- **Cross-validation:** Performed for model robustness.  

---

## 🖥️ Deployment  

The app is deployed using **Streamlit Cloud** for easy access and scalability.  

🔗 [Try It Here](https://heartdiseasepredictionap.streamlit.app/)

---

## 💡 Future Improvements  

- Integration with **FastAPI** for backend deployment  
- Containerization using **Docker**  
- Addition of **Explainable AI (SHAP plots)**  
- Integration with wearable device data  

---

## 👨‍💻 Author  

**Amit Singh**  
Machine Learning Engineer | Data Enthusiast  
🌐 [LinkedIn](https://www.linkedin.com/in/amitsingh2022/) | [GitHub](https://github.com/amitsingh2022)

---

⭐ If you like this project, give it a star on GitHub!

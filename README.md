# 🩺 Kidney Disease Prediction (Flask Web App)

---

## 📌 About Project

This project predicts Chronic Kidney Disease (CKD) using Machine Learning.

It is converted into a web application using Flask and deployed on AWS EC2.

---

## 🚀 Features

* Machine Learning model (Naive Bayes)
* Flask web application
* Input form with 24 medical features
* Auto-fill demo button
* Real-time prediction

---

## 📂 Dataset

Dataset is already included in this repository:

* dataset/train.csv
* dataset/test.csv

---

## ⚙️ How to Run on Server (EC2 / Linux)

### 🧩 Step 1: Connect to server

```bash
ssh ubuntu@YOUR-IP
```

---

### 🧩 Step 2: Clone repository

```bash
git clone https://github.com/Dinesh-9966/Chronic-Kidney-Disease.git
cd Chronic-Kidney-Disease
```

---

### 🧩 Step 3: Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🧩 Step 4: Install dependencies

```bash
pip install -r requirements.txt
pip install flask
```

---

### 🧩 Step 5: Run application

```bash
python3 webapp.py
```

---

### 🌍 Step 6: Open in browser

```
http://YOUR-IP:5000
```

---

## 🎯 Output

* CKD (Kidney Disease Detected)
* NOT CKD (Healthy)

---

## 🎓 Improvements Made

* Fixed sklearn errors
* Converted GUI project to web app
* Added frontend UI
* Added auto-fill demo feature
* Converted numeric output (1.0 → CKD)
* Deployed on AWS EC2

---

## 👨‍💻 About Me

Hi, I'm **Dinesh** 👋
I built this project as part of Machine Learning and Web Development learning.

* 🎓 Developer
* 💡 Interested in AI & ML
* 🚀 Built and deployed on AWS

---

## 🔗 Connect with Me

* GitHub: https://github.com/Dinesh-9966

---

⭐ If you like this project, give it a star!
